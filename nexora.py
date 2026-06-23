import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA", layout="centered")

# 2. تنسيق CSS: خلفية كاملة + استمارة شفافة تماماً + خطوط واضحة
st.markdown("""
    <style>
    /* صورة الخلفية */
    .stApp {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* جعل الاستمارة متناغمة (بدون مستطيل بارز) */
    .stForm {
        background: rgba(255, 255, 255, 0.9) !important;
        padding: 20px;
        border-radius: 15px;
    }
    
    /* كتابة واضحة في الخانات */
    .stTextInput input, .stSelectbox select {
        color: #000 !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    
    /* تسميات الخانات باللون الأسود الغامق */
    label {
        color: #000 !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة المتجر (بدون عناوين إضافية)
st.write("<br><br><br>", unsafe_allow_html=True)

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
            st.success("تم الإرسال!")
        else:
            st.error("يرجى ملء البيانات")
