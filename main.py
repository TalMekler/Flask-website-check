from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import functions as F

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=10)

@app.route("/")
def homePage():
    return render_template("index.html", pageTitle="Testing Home page".title(), pageHeader="YR Payroll")

if __name__ == "__main__":
    app.run(debug=True)