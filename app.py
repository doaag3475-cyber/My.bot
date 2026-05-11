```python
import telebot
import google.generativeai as genai
import PyPDF2
import os

# ====================================
# TOKENS
# ====================================

TOKEN = "PUT_TELEGRAM_TOKEN_HERE"
GEMINI_KEY = "PUT_GEMINI_KEY_HERE"

# ====================================
# GEMINI SETUP
# ====================================

genai.configure(api_key=GEMINI_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# ====================================
# TELEGRAM BOT
# ====================================

bot = telebot.TeleBot(TOKEN)

# ====================================
# PDF FILES
# ====================================

pdf_files = [
    "العناصره الغذائية والهضم.pdf",
    "هضم وتمثيل الدهون 26.pdf",
    "محاضرة هضم ةتمثيل الكربوهيردات.pdf",
    "الماء وصحةالانسان.pdf",
    "البروتين.pdf"
]

# ====================================
# READ PDF FUNCTION
# ====================================

def read_pdf(file_path):

    text = ""

    try:

        with open(file_path, "rb") as file:

            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:

                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

    except Exception as e:

        print(f"Error reading {file_path}: {e}")

    return text

# ====================================
# LOAD ALL LECTURES
# ====================================

knowledge = ""

for pdf in pdf_files:

    if os.path.exists(pdf):

        print(f"Loading: {pdf}")

        knowledge += read_pdf(pdf)

        knowledge += "\n\n"

    else:

        print(f"File not found: {pdf}")

# ====================================
# START COMMAND
# ====================================

@bot.message_handler(commands=['start'])
def start(message):

    bot.reply_to(
        message,
        "أهلاً 👋\nأنا بوت التغذية الذكي.\nاسألني أي سؤال من المحاضرات."
    )

# ====================================
# MAIN CHAT
# ====================================

@bot.message_handler(func=lambda m: True)
def reply(message):

    try:

        prompt = f"""
أنت مساعد ذكي متخصص في مادة الغذاء والتغذية.

اعتمد فقط على المعلومات الموجودة داخل المحاضرات التالية.

إذا كانت الإجابة غير موجودة داخل المنهج قل:
"المعلومة غير موجودة في المحاضرات المتاحة."

المحاضرات:
{knowledge}

السؤال:
{message.text}
"""

        response = model.generate_content(prompt)

        bot.reply_to(message, response.text)

    except Exception as e:

        print(e)

        bot.reply_to(
            message,
            "حدث خطأ أثناء معالجة السؤال."
        )

# ====================================
# RUN BOT
# ====================================

print("Bot is running...")

bot.infinity_polling()
```
