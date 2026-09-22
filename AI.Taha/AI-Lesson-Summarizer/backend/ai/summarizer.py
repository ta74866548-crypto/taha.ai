import google.generativeai as genai
import os

# لاحقاً يمكنك استبدال هذا المتغير بـ API Key الخاص بك من Google AI Studio
# أو يمكنك حفظه في ملف .env
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "ضع_مفتاحك_هنا")
genai.configure(api_key=GOOGLE_API_KEY)

def generate_summary(text):
    """
    تأخذ النص المستخرج من الدرس وتقوم بإرساله إلى نموذج الذكاء الاصطناعي (Gemini) لتلخيصه
    """
    if not text or len(text.strip()) == 0:
        return "لا يوجد نص لتلخيصه."

    # في حال لم يتم إعداد المفتاح بعد
    if GOOGLE_API_KEY == "ضع_مفتاحك_هنا":
        return f"""(ملاحظة: هذا ملخص تجريبي لأنه لم يتم إدخال Google API Key)
        
أهم النقاط في الدرس:
- الملف يحتوي على نص بطول {len(text)} حرف.
- يرجى إضافة الـ API Key في الكود لتفعيل التلخيص الحقيقي بالذكاء الاصطناعي.

مقتطف من النص الأصلي: 
{text[:200]}..."""

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"""
        قم بتلخيص الدرس التالي بطريقة مبسطة، واضحة ومقسمة إلى نقاط رئيسية لتسهيل المذاكرة.
        استخدم اللغة العربية.
        
        النص:
        {text}
        """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "حدث خطأ أثناء محاولة التلخيص."
