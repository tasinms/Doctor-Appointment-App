from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/about")
def about():
    name = 'Tasin'
    return render_template('about.html', name_temp=name)


app.run(debug=True)
