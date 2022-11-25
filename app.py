from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from docker"

@app.route("/books")
def books():
    return "books"