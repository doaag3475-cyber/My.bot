import telebot
import google.generativeai as genai

TOKEN = "8645642925:AAH2hPxrmF0WyHul sBtU PDWk8lihMzq8ppI" 
GEMINI_KEY = "AIzaSyAolC_kO-p4d9wfL9N1d-llSsLmZ4bLtLQ"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(TOKEN)

knowledge = "أهلاً بك! أنا بوت دعاء الذكي، كيف يمكنني مساعدتك اليوم؟"

@bot.message_handler(func=lambda m: True)
def reply(message):
    try:
        full_prompt = f"استخدم هذه المعلومات للرد: {knowledge}\n\nالسؤال: {message.text}"
        response = model.generate_content(full_prompt)
        bot.reply_to(message, response.text)
    except:
        bot.reply_to(message, "أنا معاك، اسألني أي حاجة!")

bot.infinity_polling()
