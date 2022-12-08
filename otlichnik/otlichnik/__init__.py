import os
import sqlite3
import click
from flask import (
    Flask, current_app, g, redirect, render_template,
    request, session, flash
)
from werkzeug.security import generate_password_hash, check_password_hash


def create_app(config=None):
    """Create Otlichnik app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, "otlichnik.db"),
        SECRET_KEY="dev",
    )
    if config is not None:
        app.config.from_mapping(config)

    @app.route("/")
    def index():
        """Render our homepage."""
        email = session.get("email", None)
        if email is not None:
            db = get_db()
            user = db.execute(
                "SELECT * from users where email=?",
                (email,)
            ).fetchone()
            g.user = user
        return render_template("index.html")

    @app.route("/signup", methods=("GET", "POST"))
    def signup():
        """Render sign-up page"""
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            db = get_db()
            error = None
            try:
                db.execute(
                    "INSERT INTO users VALUES (?, ?)",
                    (email, generate_password_hash(password))
                )
                db.commit()
            except db.IntegrityError:
                error = "User already exists."
            if not error:
                session["email"] = email
                return redirect("/")
            flash(error)

        return render_template("signup.html")

    @app.route("/signin", methods=("GET", "POST"))
    def signin():
        """Render signin page."""
        if request.method == "POST":
            email = request.form["email"]
            password = request.form["password"]
            db = get_db()
            user = db.execute(
                "SELECT * from users where email=?",
                (email,)
            ).fetchone()
            if check_password_hash(user["pwhash"], password):
                session["email"] = email
                return redirect("/")
            flash("Invalide username or password")
        return render_template("signin.html")

    @app.route("/signout")
    def signout():
        session.clear()
        return redirect("/")

    app.teardown_request(close_db)
    app.cli.add_command(init_db_command)

    return app


def get_db():
    """Return database and cache it per request."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(_exp=None):
    """Close db for request if any."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


@click.command(short_help="Create database if not exists.")
def init_db_command():
    """Command to create database if not exists."""
    init_db()


def init_db():
    """Create database if not exists."""
    os.makedirs(current_app.instance_path, exist_ok=True)
    db = get_db()
    with current_app.open_resource("schema.sql", "rt") as f:
        db.execute(f.read())
