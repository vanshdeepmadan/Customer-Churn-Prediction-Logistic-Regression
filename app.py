from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model_with_threshold.pkl')

@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Raw data received:", request.data)  # Log raw request data
        data = request.get_json()
        print("Parsed JSON:", data)  # Log parsed JSON

        if 'features' not in data:
            return jsonify({'error': "Missing 'features' key in request payload"}), 400

        features = np.array(data['features']).reshape(1, -1)
        probability = model.predict_proba(features)[0, 1]
        prediction = int(probability >= 0.4)

        return jsonify({
            'churn_probability': round(probability, 4),
            'churn_prediction': prediction
        })

    except Exception as e:
        print("Error occurred:", str(e))  # Log the error
        return jsonify({'error': str(e)}), 400
        
# Root endpoint for health check
@app.route('/')
def home():
    return "Customer Churn Prediction API is running!", 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)