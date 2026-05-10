import streamlit as st
import json

st.title("🤖 بوت المنهج الذكي")

# محاولة فتح ملف الأسئلة
try:
    with open('date.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
except:
    data = []

query = st.text_input("اسألني سؤال:")

if query:
    found = False
    for item in data:
        if query in item['question']:
            st.success(item['answer'])
            found = True
    if not found:
        st.warning("السؤال مش موجود!")
      
