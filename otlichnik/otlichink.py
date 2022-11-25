from flask import Flask

app = Flask("otlichnik")

@app.route("/")
def index():
    return "<h1>Hello World</h1>"