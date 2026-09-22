import os
import PyPDF2

def extract_text_from_file(file_path):
    """
    دالة تحدد نوع الملف وتستخرج النص منه
    """
    if not os.path.exists(file_path):
        return None
        
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.pdf':
        return read_pdf(file_path)
    else:
        # سيتم إضافة دعم استخراج النص من الصور (OCR) لاحقاً
        return "تم التعرف على الملف، ولكن ميزة استخراج النص من الصور قيد التطوير."

def read_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    return text
