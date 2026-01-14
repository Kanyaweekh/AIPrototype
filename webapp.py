from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# --- 1. ส่วนโหลดโมเดล ---
# ตรวจสอบว่ามีไฟล์โมเดลไหม ถ้าไม่มีจะแจ้งเตือน
if os.path.exists('iris_model.pkl'):
    model = joblib.load('iris_model.pkl')
    print("✅ Model loaded successfully.")
else:
    print("⚠️ WARNING: 'iris_model.pkl' not found. Please run train_model.py first.")
    model = None

class_names = ['Setosa', 'Versicolor', 'Virginica']

# --- 2. ส่วนจับคู่รูปภาพ (MAPPING) ---
# ชื่อในนี้ต้องตรงกับชื่อไฟล์ในโฟลเดอร์ static/images/
IMAGE_MAP = {
    'Setosa': 'setosa.jpg',
    'Versicolor': 'versicolor.jpg',
    'Virginica': 'virginica.jpg'
}

# --- 3. Route หน้าแรก ---
@app.route('/')
def home():
    return render_template('first.html')

# --- 4. API สำหรับทำนายผล ---
@app.route('/api/predict', methods=['POST'])
def predict_api():
    try:
        if not model:
            return jsonify({'error': 'Model not loaded (iris_model.pkl missing)'})

        # รับค่าจาก Form
        features = [
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width'])
        ]
        
        # ทำนายผล
        final_features = np.array([features])
        prediction = model.predict(final_features)
        predicted_class = class_names[prediction[0]]
        
        # ดึงชื่อไฟล์รูปภาพ
        image_file = IMAGE_MAP.get(predicted_class, 'default.jpg')
        
        # ส่งผลลัพธ์กลับไปเป็น JSON
        return jsonify({
            'class': predicted_class,
            'image_file': image_file
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

# --- 5. Route พิเศษสำหรับตรวจสอบไฟล์ (DEBUG) ---
# เข้าใช้งานโดยไปที่: http://localhost:5002/check-files
@app.route('/check-files')
def check_files():
    # ดูว่าโปรแกรมรันจากโฟลเดอร์ไหน
    current_folder = os.getcwd()
    
    # สร้าง path ไปยังโฟลเดอร์รูปภาพ
    images_folder = os.path.join(current_folder, 'static', 'images')
    
    # เช็คว่ามีโฟลเดอร์ไหม
    if os.path.exists(images_folder):
        status = "✅ Found folder (เจอโฟลเดอร์)"
        try:
            files = os.listdir(images_folder) # อ่านรายชื่อไฟล์
        except Exception as e:
            files = f"Error reading files: {str(e)}"
    else:
        status = "❌ FOLDER NOT FOUND (หาโฟลเดอร์ไม่เจอ!!)"
        files = []

    # แสดงผลเป็น JSON บนหน้าเว็บ
    return jsonify({
        "1_Current_Working_Directory (รันจากที่นี่)": current_folder,
        "2_Target_Images_Folder (ระบบมองหาที่นี่)": images_folder,
        "3_Status": status,
        "4_Files_Found_In_Folder (ไฟล์ที่เจอ)": files
    })

if __name__ == "__main__":
    # รันบน Port 5002
    app.run(host='0.0.0.0', debug=True, port=8003)

