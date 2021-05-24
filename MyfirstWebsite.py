from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>WELCOME CHAMP</p>"

@app.route("/aboutus")
def aboutus():
    return "<h1>IT solutions and Computer repairs</h1>"

@app.route("/contactus")
def contactus():
    return "<h1>For more information, call 08136690458</h1>"

@app.route("/products")
def products():
    return "<h1>File servers</h1>"

@app.route("/services")
def services():
    return "<h1>We offer cloud services and IT/Tech support.</h1>"