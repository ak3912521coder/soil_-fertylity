from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("soil_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    
    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    pH = float(request.form["pH"])
    OC = float(request.form["OC"])

    
    features = np.array([[N, P, K, pH, OC]])
    prediction = model.predict(features)[0]

    
    if prediction == "High":
        result = "Soil Fertility: High. This soil is highly suitable for farming."
    elif prediction == "Medium":
        result = "Soil Fertility: Medium. The soil is moderately fertile and may require some fertilizer."
    else:
        result = "Soil Fertility: Low.This soil is not suitable for farming and requires additional nutrients."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
