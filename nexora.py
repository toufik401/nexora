import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA STORE", layout="centered")

# 2. CSS للخلفية الكاملة (تظهر في الهاتف والكمبيوتر)
st.markdown("""
    <style>
    /* جعل صورة الشعار خلفية كاملة للموقع */
    .stApp {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    
    /* طبقة شفافة لتسهيل قراءة الاستمارة فوق الخلفية */
    .form-container {
        background: rgba(0, 0, 0, 0.75);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #3b82f6;
        color: white;
    }
    
    /* جعل الكتابة داخل المربعات باللون الأسود */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        color: black !important;
        background-color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 3. واجهة المتجر
st.markdown("<br><br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='form-container'>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #3b82f6;'>NEXORA STORE</h1>", unsafe_allow_html=True)
    
    with st.form("customerForm"):
        name = st.text_input("الاسم الكامل:")
        province = st.selectbox("الولاية:", ["الجزائر", "الأغواط", "قسنطينة", "ورقلة", "سطيف"])
        phone = st.text_input("رقم الهاتف:")
        insta = st.text_input("رابط أو اسم الإنستغرام:")
        
        submit = st.form_submit_button("إرسال الطلب الآن 🚀")
        
        if submit:
            if name and phone:
                token = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'
                chat_id = '7055252264'
                msg = f"🛒 طلب جديد NEXORA\n👤 {name}\n📍 {province}\n📞 {phone}\n📸 {insta}"
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
                st.balloons()
                st.success("تم إرسال طلبك بنجاح!")
            else:
                st.error("يرجى ملء الاسم ورقم الهاتف.")
    st.markdown("</div>", unsafe_allow_html=True)
