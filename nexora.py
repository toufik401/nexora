import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA STORE", layout="centered")

# 2. تنسيق احترافي (خلفية سوداء بالكامل وتركيز على الشعار)
st.markdown("""
    <style>
    /* خلفية سوداء بالكامل للمتجر */
    .stApp { background-color: #000000; font-family: sans-serif; }
    
    /* الشعار يظهر بوضوح وبدون حواف */
    .logo-container { text-align: center; margin-bottom: 30px; }
    .logo-img { max-width: 100%; height: auto; border-radius: 10px; }
    
    /* استمارة الطلب بشكل أنيق */
    .form-box { 
        background: #111; 
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid #333;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.2); 
    }
    
    /* جعل الكتابة داخل الخانات باللون الأسود للوضوح */
    .stTextInput > div > div > input { color: #000 !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 3. عرض الشعار (بشكل كبير وواضح)
st.markdown("<div class='logo-container'>", unsafe_allow_html=True)
st.image("https://i.ibb.co/v413XTWG/1782140096443.png", width=400) 
st.markdown("</div>", unsafe_allow_html=True)

# 4. الاستمارة
with st.container():
    st.markdown("<div class='form-box'>", unsafe_allow_html=True)
    with st.form("customerForm"):
        st.subheader("📝 طلب خدمة جديدة")
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
                st.success("تم استلام طلبك، شكراً لاختيارك NEXORA!")
            else:
                st.error("يرجى ملء الاسم ورقم الهاتف.")
    st.markdown("</div>", unsafe_allow_html=True)
