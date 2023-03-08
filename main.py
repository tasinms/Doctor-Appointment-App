from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/login")
def login():
    return render_template('login.html')


# @app.route("/about")
# def about():
#     name = 'Tasin'
#     return render_template('about.html', name_temp=name)


app.run(debug=True)
