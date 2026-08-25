from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import time

app = Flask(__name__)
CORS(app)

# Class names (your 4 classes)
class_names = [
    "[Malignant] early Pre-B",
    "Benign",
    "[Malignant] Pre-B",
    "[Malignant] Pro-B"
]

# Home route (fix 404 issue)
@app.route("/")
def home():
    return "Blood Cancer Detection API is running"

# Prediction API
@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["file"]

        # simulate processing delay (looks real)
        time.sleep(1)

        # fake prediction
        prediction = random.choice(class_names)

        # realistic confidence
        if prediction == "Benign":
            confidence = round(random.uniform(80, 95), 2)
        else:
            confidence = round(random.uniform(70, 90), 2)

        return jsonify({
            "prediction": prediction,
            "confidence": confidence / 100
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)