import streamlit as st
import pandas as pd
import requests
# 2. حقن CSS للتحكم في الألوان، الشفافية، والخلفية
st.markdown("""
    <style>
    /* خلفية الصفحة */
    .stApp {
        background: url('https://i.ibb.co/v413XTWG/1782140096443.png');
        background-size: cover;
    }
    div[data-baseweb="input"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border: 1px solid white !important;
    }
    input { color: white !important; }
    label { color: white !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. لوحة تحكم المالك (مخفية عبر كلمة سر)
if "logged_in" not in st.session_state: st.session_state.logged_in = False

with st.sidebar:
    st.subheader("إعدادات المالك")
    password = st.text_input("كلمة مرور الإدارة", type="password")
    if password == "1234": # غيّر كلمة السر هنا
        st.session_state.logged_in = True
        st.write("تم الدخول للوحة التحكم")
    
    if st.session_state.logged_in:
        st.color_picker("اختر لون الخط", "#FFFFFF")
        st.file_uploader("تغيير صورة الخلفية")

# 4. واجهة الزبون
st.title("🛍️ متجر Nexora")

with st.form("order_form"):
    name = st.text_input("الاسم")
    state = st.text_input("الولاية")
    phone = st.text_input("رقم الهاتف")
    insta = st.text_input("حساب انستغرام أو رابط")
    trade_type = st.selectbox("نوع التجارة الخاصة بك", ["مواد غذائية", "ألبسة", "مأكولات", "حلويات"])
    
    submit = st.form_submit_button("إرسال الطلب")

# 5. إرسال الطلب إلى تيليجرام
def send_to_telegram(text):
    token = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
    chat_id = "7055252264"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)

if submit:
    order_data = f"طلب جديد من {name}، الولاية: {state}، الهاتف: {phone}، النشاط: {trade_type}"
    send_to_telegram(order_data)
    
    # 8. تأثير النجوم الذهبية
    st.balloons() 
    st.success("تم إرسال طلبك بنجاح! ⭐⭐⭐")
