
import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="معاً لنطور تجارة مدينتنا", layout="centered")

# 2. CSS للخلفية والعنوان الذهبي
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/dark-background-with-golden-lines_1017-27083.jpg");
        background-size: cover;
    }
    .gold-title { 
        text-align: center; color: #D4AF37; border: 3px solid #D4AF37; 
        padding: 15px; border-radius: 20px; background: rgba(0, 0, 0, 0.8); 
    }
    .content-box { background: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)

# 3. إعدادات البيانات (الحالة)
if 'img' not in st.session_state: st.session_state.img = "https://i.ibb.co/27SxJFCY/IMG-20260621-230717-021.jpg"
if 'price' not in st.session_state: st.session_state.price = "1000"

# 4. لوحة تحكم المالك
st.sidebar.title("🛠️ لوحة تحكم المالك")
pwd = st.sidebar.text_input("كلمة سر المالك", type="password")
if pwd == "1234":
    st.session_state.img = st.sidebar.text_input("رابط صورة المنتج:", st.session_state.img)
    st.session_state.price = st.sidebar.text_input("تعديل السعر:", st.session_state.price)
    st.sidebar.success("تم تحديث البيانات!")

# 5. واجهة المتجر
st.markdown("<div class='gold-title'><h1>✨ معاً لنطور تجارة مدينتنا ✨</h1></div>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.markdown("<a href="https://ibb.co/TMc4W7GS"><img src="https://i.ibb.co/v413XTWG/1782140096443.png" alt="1782140096443" border="0"></a><br /><a target='_blank' href='https://usefulwebtool.com/fr/convertir-texte-en-binaire'>que veut dire binaire</a><br />")
    st.image(st.session_state.img, use_container_width=True)
    st.markdown(f"<h2 style='text-align: center; color: black;'>السعر: {st.session_state.price} دج</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 6. نموذج الفاتورة
st.write("<br>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.subheader("📝 طلب فاتورة جديدة")
    with st.form("invoice_form", clear_on_submit=True):
        name = st.text_input("الاسم الكريم (إجباري)")
        phone = st.text_input("رقم الهاتف (إجباري)")
        trade_type = st.selectbox("نوع التجارة", ["مواد غذائية", "مأكولات", "حلويات", "ألبسة"])
        submit = st.form_submit_button("إرسال الطلب (تليجرام)")
        
        if submit:
            if name and phone:
                token = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
                chat_id = "7055252264"
                msg = f"🛒 طلب جديد!\nالاسم: {name}\nالهاتف: {phone}\nالنشاط: {trade_type}\nالسعر: {st.session_state.price}"
                requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
                st.balloons()
                st.success("تم إرسال طلبك بنجاح!")
            else:
                st.error("يرجى ملء البيانات المطلوبة")
    st.markdown("</div>", unsafe_allow_html=True)
