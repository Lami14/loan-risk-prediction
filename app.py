from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/loan_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Loan Risk Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    features = np.array([[
        data['income'],
        data['credit_score'],
        data['loan_amount'],
        data['employment_years'],
        data['debt_to_income']
    ]])
    
    prediction = model.predict(features)[0]
    result = "Approved" if prediction == 1 else "Rejected"
    
    return jsonify({'loan_status': result})

if __name__ == '__main__':
    app.run(debug=True)
