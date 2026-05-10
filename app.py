import telebot
import google.generativeai as genai

# 1. حطي التوكن ومفتاح جيمناي هنا
TOKEN = "75432XXXXX:AAXXXXX..." 
GEMINI_KEY = "AIzaSyXXXXX..."

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN)

# 2. هنا بقى اكتبي كل المعلومات اللي في الـ PDF (اكتبيها بايدك باختصار)
knowledge = """
اكتبي هنا كل المعلومات اللي كانت في الملفات.. 
مثلاً: البوت ده بيساعد في كذا.. 
ومواعيدنا كذا.. 
والأسعار كذا..
كل اللي تعرفيه اكتبيه هنا بين العلامات دي.
"""

@bot.message_handler(func=lambda m: True)
def reply(message):
    prompt = f"بناءً على المعلومات دي: {knowledge}\n\nجاوب على المستخدم: {message.text}"
    response = model.generate_content(prompt)
    bot.reply_to(message, response.text)

bot.infinity_polling()
