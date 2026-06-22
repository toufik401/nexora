import streamlit as st
import requests

# 1. إعداد الصفحة لتكون نظيفة (بدون إطارات)
st.set_page_config(page_title="Nexora Store", layout="centered")

# 2. التنسيق (CSS) للألوان (خلفية سوداء للكتابة، خط أبيض، وتنسيق العنوان)
st.markdown("""
    <style>
    /* جعل الخلفية العامة للصورة */
    .stApp {
        background-image: url('https://i.ibb.co/v413XTWG/1782140096443.png');
        background-size: cover;
    }
    /* تنسيق منطقة الكتابة */
    .stTextInput > div > div > input {
        background-color: black !important;
        color: white !important;
        border: 1px solid white;
    }
    /* العنوان الكبير المزخرف */
    .title-text {
        font-family: 'Courier New', Courier, monospace;
        font-size: 50px;
        color: white;
        text-align: center;
        text-shadow: 2px 2px 4px #000000;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.markdown('<p class="title-text">✨ Nexora Store ✨</p>', unsafe_allow_html=True)

# 3. نموذج الطلبيات (الاسم، الهاتف، الانستغرام)
st.write("### 📝 تفاصيل الطلب")
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")
insta = st.text_input("حساب الانستغرام")

# 4. إرسال الطلبية إلى بوت تليجرام
def send_to_telegram(message):
    token = "توكن_البوت_الخاص_بك"
    chat_id = "الايدي_الخاص_بك"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

if st.button("إرسال الطلب"):
    if name and phone:
        msg = f"طلب جديد من متجر Nexora:\nالاسم: {name}\nالهاتف: {phone}\nالانستغرام: {insta}"
        send_to_telegram(msg)
        st.success("تم إرسال طلبك بنجاح! 🎉")
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف على الأقل.")

# 5. البالونات في النهاية
st.balloons()
