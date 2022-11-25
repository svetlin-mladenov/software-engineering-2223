from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Renders our homepage."""
    return "<h1>Hello World</h1>"
