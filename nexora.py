import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="Nexora Service", layout="centered")

# 2. حقن كود الـ CSS الخاص بك بالكامل
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@500;700&display=swap');
    
    .stApp { background-color: #0f172a; font-family: 'Reem Kufi', sans-serif; }
    
    .kufi-title { font-size: 2rem; font-weight: 700; color: #ffffff; text-align: center; margin-top: 20px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
    
    .order-form { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.1); }
    
    .stTextInput > div > div > input, .stSelectbox > div > div > div { background: rgba(15, 23, 42, 0.6) !important; color: white !important; border: 1px solid rgba(255, 255, 255, 0.2) !important; }
    
    .stButton > button { width: 100%; background-color: #3b82f6 !important; color: white !important; font-weight: bold; border: none; padding: 14px; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# 3. الواجهة
st.markdown("<h1 class='kufi-title'>مرحبا بيك في خدمة Nexora</h1>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500", use_column_width=True)

# 4. الاستمارة
with st.container():
    st.markdown("<div class='order-form'>", unsafe_allow_html=True)
    with st.form("customerForm"):
        name = st.text_input("الاسم الكامل:")
        province = st.selectbox("الولاية:", ["الجزائر", "الأغواط", "قسنطينة", "ورقلة", "سطيف"])
        phone = st.text_input("رقم الهاتف:")
        insta = st.text_input("حساب الانستغرام:")
        
        submit = st.form_submit_button("تأكيد إرسال الطلب ✨")
        
        if submit:
            if name and phone:
                token = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'
                chat_id = '7055252264'
                msg = f"🚀 طلب جديد لمتجر Nexora\n👤 الاسم: {name}\n📍 الولاية: {province}\n📞 الهاتف: {phone}\n📸 انستغرام: {insta}"
                
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
                st.balloons()
                st.success("تم إرسال طلبك بنجاح!")
            else:
                st.warning("يرجى ملء البيانات!")
    st.markdown("</div>", unsafe_allow_html=True)
