from flask import Flask, jsonify    # Flask - API'S  jsonify - response in json format
# Ex. fare for 10km ? ---> {"fare":230}
from sklearn.linear_model import LinearRegression   # y = mx + c
import pandas as pd
app = Flask(__name__)       # app - GET,POST,PUT,DELETE
# ==========================================
# 1. Load Dataset
# ==========================================
df = pd.read_csv("fare.csv")
X = df[["distance"]]
y = df["fare"]
# ==========================================
# 2. Create Linear Regression Model
# ==========================================
model = LinearRegression()
# ==========================================
# 3. Train Model
# ==========================================
model.fit(X, y)

print("Model trained successfully")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)


# ==========================================
# 4. Home Route
# ==========================================
@app.route("/")
def home():
    return "Linear Regression ML API is running!"


# ==========================================
# 5. Prediction Route
# ==========================================
@app.route("/predict/<float:distance>")     # http://127.0.0.1:5001/predict/6.0 --> {"fare":200}
def predict(distance):

    # Convert input into DataFrame
    input_data = pd.DataFrame({
        "distance": [distance]
    })

    # Predict fare
    prediction = model.predict(input_data)

    fare = prediction[0]

    return jsonify({
        "distance": distance,
        "predicted_fare": round(float(fare), 2)
    })
# ==========================================
# 6. Start Flask Application
# ==========================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5001,
        debug=True
    )