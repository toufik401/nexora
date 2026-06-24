import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="NEXORA", layout="centered")

# 2. حقن CSS (الحل النهائي لتثبيت الخلفية على الهاتف والكمبيوتر)
st.markdown("""
    <style>
    /* فرض الخلفية على كامل الشاشة */
    html, body, [data-testid="stAppViewContainer"] {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png") !important;
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        background-repeat: no-repeat !important;
    }
    
    /* جعل كل الحاويات شفافة لتظهر الخلفية */
    .stApp, div[data-testid="stVerticalBlock"], div[data-testid="stForm"] {
        background: transparent !important;
    }
    
    /* تنسيق المربعات لتكون واضحة */
    .stTextInput > div > div > input, .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.9) !important;
        color: black !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. لوحة تحكم المالك
if "logged_in" not in st.session_state: st.session_state.logged_in = False

with st.sidebar:
    st.subheader("إعدادات المالك")
    password = st.text_input("كلمة مرور الإدارة", type="password")
    if password == "1234":
        st.session_state.logged_in = True
    
    if st.session_state.logged_in:
        st.write("✅ تم الدخول للإدارة")
        if st.button("حفظ الإعدادات"):
            st.success("تم الحفظ!")

# 4. واجهة الزبون
st.title("🛍️ متجر Nexora")

with st.form("order_form"):
    name = st.text_input("الاسم")
    state = st.text_input("الولاية")
    phone = st.text_input("رقم الهاتف")
    insta = st.text_input("حساب انستغرام أو رابط")
    trade_type = st.selectbox("نوع التجارة", ["مواد غذائية", "ألبسة", "مأكولات", "حلويات"])
    
    submit = st.form_submit_button("إرسال الطلب")

# 5. منطق إرسال الطلب
if submit:
    if name and phone:
        token = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'
        chat_id = '7055252264'
        
        # تنسيق الفاتورة
        invoice_msg = (
            f"🧾 **فاتورة طلب جديدة من Nexora**\n"
            f"━━━━━━━━━━━━━━\n"
            f"👤 **الاسم:** {name}\n"
            f"📍 **الولاية:** {state}\n"
            f"📞 **الهاتف:** {phone}\n"
            f"🍱 **نوع التجارة:** {trade_type}\n"
            f"📸 **حساب إنستغرام:** {insta}\n"
            f"━━━━━━━━━━━━━━\n"
            f"✅ تم استلام الطلب بنجاح"
        )
        
        requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage", 
            data={"chat_id": chat_id, "text": invoice_msg, "parse_mode": "Markdown"}
        )
        
        st.balloons()
        st.success("تم إرسال طلبك بنجاح! ⭐⭐⭐")
    else:
        st.error("يرجى ملء البيانات المطلوبة (الاسم والهاتف).")

