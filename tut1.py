from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"


@app.route("/tasin")
def tasin():
    return "<p>Hello, Tasin! How you doin!</p>"


app.run(debug=True)
