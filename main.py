from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json', 'r') as c:
    parameters = json.load(c)['parameters']
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/doccure"
db.init_app(app)


class Patients(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Fetch Variables From HTML File
        name = request.form.get("name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        password = request.form.get("password")

        # Add Entry To DataBase
        entry = Patients(name=name, email=email, phone_number=phone_number, password=password)
        db.session.add(entry)
        db.session.commit()

    return render_template('register.html')


@app.route("/login")
def login():
    return render_template('login.html')


# @app.route("/about")
# def about():
#     name = 'Tasin'
#     return render_template('about.html', name_temp=name)

print('Running...')

app.run(debug=True)
