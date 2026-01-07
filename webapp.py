# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load('iris_model.pkl')
class_names = ['Setosa', 'Versicolor', 'Virginica']

@app.route('/')
def home():
    # เรียกไฟล์จาก folder 'templates' โดยอัตโนมัติ
    return render_template('first.html')

@app.route('/api/predict', methods=['POST'])
def predict_api():
    try:
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        
        final_features = np.array([features])
        prediction = model.predict(final_features)
        predicted_class = class_names[prediction[0]]
        
        return jsonify({'class': predicted_class})
        
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":   # run code 
    app.run(host='localhost',debug=True,port=5002)#host='0.0.0.0' = run on internet ,port=5001