import os
import PyPDF2
# هتحتاج مكتبة الذكاء الاصطناعي اللي كنا شغالين بيها (مثلاً Gemini)
import google.generativeai as genai

# دالة لقراءة كل النصوص من ملفات الـ PDF في المجلد
def load_all_pdfs():
    context = ""
    for file in os.listdir():
        if file.endswith(".pdf"):
            with open(file, 'rb') as f:
                pdf_reader = PyPDF2.PdfReader(f)
                for page in pdf_reader.pages:
                    context += page.extract_text()
    return context

# هنا بنجهز البوت بالمعلومات اللي قراها
all_info = load_all_pdfs()

# كود الرد (الرد بناءً على الـ all_info)
# ... كمل باقي كود الربط بـ Telegram أو الشات بتاعك ...

