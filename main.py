from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

local_server = True
with open('config.json', 'r') as c:
    parameters = json.load(c)['parameters']

db = SQLAlchemy()
app = Flask(__name__)

if local_server:
    app.config["SQLALCHEMY_DATABASE_URI"] = parameters['local_uri']
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = parameters['host_uri']

db.init_app(app)


class Patients(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(30), unique=False, nullable=False)


class Doctors(db.Model):
    doctor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    doctor_image = db.Column(db.String(20), unique=False, nullable=True)
    doctor_thumb_image = db.Column(db.String(20), unique=False, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=False)
    speciality = db.Column(db.String(30), unique=False, nullable=False)
    department = db.Column(db.String(30), unique=False, nullable=False)
    location = db.Column(db.String(30), unique=False, nullable=False)
    overview = db.Column(db.String(30), unique=False, nullable=False)
    fee = db.Column(db.Integer, unique=False, nullable=False)
    slug = db.Column(db.String(30), unique=True, nullable=False)


@app.route("/")
def home():
    doctors = Doctors.query.filter_by().all()
    return render_template('index.html', parameters=parameters, doctors=doctors)


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

    return render_template('register.html', parameters=parameters)


@app.route("/doctor-profile/<string:doctor_profile_slug>", methods=['GET'])
def doctor_profile(doctor_profile_slug):
    doctor = Doctors.query.filter_by(slug=doctor_profile_slug).first()
    return render_template('doctor-profile.html', parameters=parameters, doctor=doctor)


@app.route("/login")
def login():
    return render_template('login.html', parameters=parameters)


# @app.route("/about")
# def about():
#     name = 'Tasin'
#     return render_template('about.html', name_temp=name)

app.run(debug=True)
