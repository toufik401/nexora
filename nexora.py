import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA - خدمة احترافية", layout="centered")

# 2. تنسيق CSS احترافي (زجاجي شفاف)
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    /* جعل المربعات زجاجية شفافة */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 12px !important;
        font-weight: bold;
    }
    /* تنسيق العناوين (Label) */
    label { color: #ffffff !important; font-size: 18px !important; font-weight: bold !important; }
    
    /* زر الإرسال */
    .stButton > button {
        background: #3b82f6 !important;
        color: white !important;
        border-radius: 10px !important;
        width: 100%;
        padding: 12px;
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الكبير والترحيب
st.markdown("<h1 style='text-align: center; color: white; font-size: 3em;'>✨ مرحباً بك في خدمتنا ✨</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #3b82f6;'>بدون أي اشتراك شهري - متجر إلكتروني خاص بك</h3>", unsafe_allow_html=True)
st.write("<br>")

# 4. الاستمارة
with st.form("clean_form"):
    st.markdown("<h3 style='color: white;'>اختر نوع تجارتك:</h3>", unsafe_allow_html=True)
    business_type = st.selectbox("", ["حلويات", "ألبسة", "مواد غذائية", "مأكولات"])
    
    name = st.text_input("الاسم الكامل")
    phone = st.text_input("رقم الهاتف")
    insta = st.text_input("حساب الإنستغرام")
    
    submit = st.form_submit_button("إرسال الطلب الآن 🚀")
    
    if submit:
        if name and phone:
            token = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'
            chat_id = '7055252264'
            msg = f"🛒 طلب جديد لمتجر Nexora\nنوع التجارة: {business_type}\nالاسم: {name}\nالهاتف: {phone}\nإنستغرام: {insta}"
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
            
            # تأثير النجاح (نجوم وخيوط ملونة)
            st.balloons()
            st.success("تم إرسال طلبك بنجاح! سنتواصل معك قريباً.")
        else:
            st.error("يرجى ملء البيانات المطلوبة.")
