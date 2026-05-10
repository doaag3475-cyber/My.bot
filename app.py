
  import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

st.set_page_config(page_title="بوت المنهج الذكي", layout="wide")
st.title("📚 بوت المنهج الذكي (إصدار الـ PDF)")

# السطر اللي جاي ده هو اللي هنحط فيه المفتاح لما نجيبه
api_key = "ضع_المفتاح_هنا" 
genai.configure(api_key=api_key)

uploaded_files = st.file_uploader("ارفع ملفات المنهج (PDF)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for file in uploaded_files:
        reader = PdfReader(file)
        for page in reader.pages:
            all_text += page.extract_text()
    
    st.success("تم تجهيز المنهج بنجاح!")
    user_question = st.text_input("اسأل أي سؤال في المنهج:")
    
