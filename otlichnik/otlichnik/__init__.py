import os
import sqlite3
import click
from flask import Flask, redirect, render_template, request

app = Flask(__name__, instance_relative_config=True)


@app.route("/")
def index():
    """Render our homepage."""
    return render_template("index.html")


@app.route("/signup", methods=("GET", "POST"))
def signup():
    """Render sign-up page"""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(f"create user {email} {password}")
        return redirect("/")

    return render_template("signup.html")


@click.command(short_help="Create database if not exists.")
def init_db():
    """Create database if not exists."""
    os.makedirs(app.instance_path, exist_ok=True)
    db_filename = os.path.join(app.instance_path, "otlichnik.db")
    db = sqlite3.connect(db_filename)
    with app.open_resource("schema.sql", "rt") as f:
        db.execute(f.read())


app.cli.add_command(init_db)
