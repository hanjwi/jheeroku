from application import app
from flask import render_template, request, json, jsonify
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
import requests
import numpy
import pandas as pd



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/strokeclassify",methods=['GET','POST'])
def strokeclassify():
    age = request.form.get("age")
    avg_glucose_level = request.form.get("avg_glucose_level")
    bmi = request.form.get("bmi")
    gender = request.form.get("gender")
    married = request.form.get("married")
    work_type = request.form.get("work_type")
    Residence_type = request.form.get("Residence_type")
    smoking_status = request.form.get("smoking_status")
    hypertension = request.form.get("hypertension")
    heart_desease = request.form.get("heart_desease")
    input_data = json.dumps({"age": age, "avg_glucose_level": avg_glucose_level, "bmi": bmi, "gender": gender, "married": married, "work_type": work_type, "Residence_type": Residence_type, "smoking_status": smoking_status, "hypertension": hypertension, "heart_desease": heart_desease})
    url = "https://heroku-test-stroke-model.herokuapp.com/api"
    results = requests.post(url, input_data)
    return render_template("index.html", age = age, avg_glucose_level = avg_glucose_level, bmi=bmi, gender=gender, married=married, work_type=work_type, Residence_type=Residence_type, smoking_status=smoking_status, hypertension=hypertension, heart_desease = heart_desease, results = results.content.decode('UTF-8'))

