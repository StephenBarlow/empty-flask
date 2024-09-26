from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/dessert")
def delicious():
    return "<p>Delicious!</p>"
