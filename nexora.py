import streamlit as st
import requests

# 1. إعداد الصفحة
st.set_page_config(page_title="Nexora Store", layout="centered")

# 2. تنسيق CSS المخصص للخطوط والألوان
st.markdown("""
    <style>
    /* تغيير لون وحجم الخط الخاص بالتسميات (Labels) ليصبح أبيض وكبير */
    label {
        color: white !important;
        font-size: 22px !important;
        font-weight: bold !important;
    }
    
    /* تغيير لون منطقة الكتابة لتكون سوداء والخط أبيض */
    .stTextInput > div > div > input {
        background-color: black !important;
        color: white !important;
        border: 2px solid white !important;
        font-size: 18px !important;
    }
    
    /* تنسيق العنوان الكبير المزخرف */
    .title-text {
        font-size: 60px !important;
        color: white !important;
        text-align: center;
        text-shadow: 4px 4px 8px #000000;
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان
st.markdown('<p class="title-text">✨ Nexora Store ✨</p>', unsafe_allow_html=True)

# 4. الحقول المطلوبة
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")
insta = st.text_input("حساب الانستغرام")

# 5. وظيفة إرسال الطلبية إلى بوت تليجرام
def send_to_telegram(message):
    # ضع هنا التوكن الخاص ببوتك والـ chat_id الخاص بك
    token = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
    chat_id = "7055252264"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url)
    except:
        st.error("حدث خطأ في الاتصال بالبوت.")

# 6. زر الإرسال
if st.button("إرسال الطلب"):
    if name and phone:
        msg = f"📦 طلب جديد من متجر Nexora:\nالاسم: {name}\nالهاتف: {phone}\nالانستغرام: {insta}"
        send_to_telegram(msg)
        st.success("تم إرسال طلبك بنجاح! 🎉")
        st.balloons()  # البالونات تظهر عند النجاح
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف على الأقل.")
