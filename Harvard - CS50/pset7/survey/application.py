import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # check if all inputs are provided
    name = request.form.get("name")
    email = request.form.get("email")
    education = request.form.get("education")
    resume = request.form.get("resume")
    prob = request.form.get("prob")
    cpp = request.form.get("cpp")
    consent = request.form.get("consent")
    subscription = request.form.get("subscription")
    if not name or not email or not education or not prob or not cpp or not consent:
        return render_template("error.html", message="Submission failed. You need to provide all required fields before submitting a form. Click the \"Form\" tab above to return.")
    # clean inputs for display
    resumeStr = "Submitted" if resume else "Not Submitted"
    subscriptionStr = "Subscribed" if subscription else "Not Subscribed"
    codingNameList = ["Python", "R", "MATLAB", "SQL"]
    codingList = []
    for codingName in codingNameList:
        if request.form.get(codingName):
            codingList.append(codingName)
    codingStr = ", ".join(codingList)
    if not codingStr:
        codingStr = "-"
    # write cleaned info into csv
    infoTuple = (name, email, education, resumeStr, prob, cpp, codingStr, subscriptionStr)
    with open("survey.csv", "a") as file:
        csv.writer(file).writerow(infoTuple)
    return redirect("/sheet")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    # read from csv and pass to display dynamically in /sheet
    with open("survey.csv", "r") as file:
        info = list(csv.reader(file))
        return render_template("surveyed.html", info=info)
