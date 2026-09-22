from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import sys

# إضافة مجلدات الباك-إند للمسار عشان نقدر نستدعي الملفات
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.file_reader import extract_text_from_file
from ai.summarizer import generate_summary

app = Flask(__name__)
CORS(app) # السماح للـ Frontend بالتواصل مع الـ Backend

@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "message": "مرحباً بك في API مُلخص الدروس الذكي"
    })

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "لم يتم إرسال ملف"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "لم يتم اختيار ملف"}), 400
        
    upload_folder = '../uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    
    return jsonify({
        "status": "success",
        "message": "تم الرفع بنجاح",
        "file_path": file_path
    })

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    file_path = data.get('file_path')
    
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "مسار الملف غير صحيح أو الملف غير موجود"}), 400
        
    # قراءة النص من الملف
    text = extract_text_from_file(file_path)
    
    if not text:
        return jsonify({"error": "لم نتمكن من استخراج النص من الملف. قد يكون الملف فارغاً أو بصيغة غير مدعومة حالياً."}), 500
        
    # تلخيص النص باستخدام الذكاء الاصطناعي
    summary = generate_summary(text)
    
    return jsonify({
        "status": "success",
        "summary": summary
    })

if __name__ == '__main__':
    # التأكد من وجود مجلد الرفع
    if not os.path.exists('../uploads'):
        os.makedirs('../uploads')
        
    app.run(debug=True, port=5000)
