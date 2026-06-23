import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA", layout="centered")

# 2. تنسيق CSS: خلفية شفافة ومسافات واضحة
st.markdown("""
    <style>
    /* صورة الخلفية */
    .stApp {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* جعل الاستمارة شفافة تماماً */
    .stForm {
        background: transparent !important;
        border: none !important;
    }
    
    /* إضافة مسافة بين الخانات */
    .stTextInput, .stSelectbox {
        margin-bottom: 25px !important;
    }
    
    /* تنسيق الخانات (لون الكتابة أسود داخل خانة بيضاء شفافة قليلاً للوضوح) */
    .stTextInput input, .stSelectbox select {
        color: #000 !important;
        background-color: rgba(255, 255, 255, 0.8) !important;
        font-weight: bold !important;
        border-radius: 10px !important;
    }
    
    /* عناوين الخانات باللون الأبيض ليظهروا فوق الخلفية */
    label {
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة الطلب
st.write("<br><br>", unsafe_allow_html=True)

with st.form("clean_form"):
    name = st.text_input("الاسم الكامل")
    province = st.selectbox("الولاية", ["الجزائر", "الأغواط", "قسنطينة", "ورقلة", "سطيف"])
    phone = st.text_input("رقم الهاتف")
    insta = st.text_input("حساب الإنستغرام")
    
    submit = st.form_submit_button("إرسال الطلب")
    
    if submit:
        if name and phone:
            token = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'
            chat_id = '7055252264'
            msg = f"🛒 طلب جديد NEXORA\nالاسم: {name}\nالولاية: {province}\nالهاتف: {phone}\nإنستغرام: {insta}"
            requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
            st.balloons()
            st.success("تم الإرسال بنجاح!")
        else:
            st.error("يرجى ملء البيانات")
