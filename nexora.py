import streamlit as st
import requests

# 1. إعدادات الصفحة
st.set_page_config(page_title="متجر NEXORA", layout="centered")

# 2. CSS للخلفية والعناصر
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://i.ibb.co/v413XTWG/1782140096443.png");
        background-size: cover;
        background-attachment: fixed;
    }
    .gold-title { 
        text-align: center; color: #D4AF37; border: 3px solid #D4AF37; 
        padding: 15px; border-radius: 20px; background: rgba(0, 0, 0, 0.9); 
    }
    .content-box { background: rgba(255, 255, 255, 0.95); padding: 20px; border-radius: 15px; }
    </style>
""", unsafe_allow_html=True)


if 'available' not in st.session_state: st.session_state.available = True

# 4. لوحة تحكم المالك
st.sidebar.title("🛠️ لوحة تحكم المالك")
pwd = st.sidebar.text_input("كلمة سر المالك", type="password")
if pwd == "1234":
    st.session_state.img = st.sidebar.text_input("رابط صورة المنتج:", st.session_state.img)
    st.session_state.price = st.sidebar.text_input("تعديل السعر:", st.session_state.price)
    st.session_state.available = st.sidebar.checkbox("المنتج متوفر؟", st.session_state.available)
    st.sidebar.success("تم التحديث!")

# 5. واجهة المتجر
st.markdown("<div class='gold-title'><h1>✨ متجر NEXORA ✨</h1></div>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    
    # حالة غير متوفر
    if not st.session_state.available:
        st.markdown("""
            <div style="text-align: center; margin-bottom: 10px;">
                <h1 style="color: red; background: white; padding: 10px; border-radius: 10px; border: 2px solid red;">
                ❌ غير متوفر حالياً ❌
                </h1>
            </div>
        """, unsafe_allow_html=True)
    
    st.image(st.session_state.img, use_container_width=True)
    st.markdown(f"<h2 style='text-align: center; color: black;'>السعر: {st.session_state.price} دج</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# 6. نموذج الفاتورة
st.write("<br>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='content-box'>", unsafe_allow_html=True)
    st.subheader("📝 طلب فاتورة جديدة")
    with st.form("invoice_form", clear_on_submit=True):
        name = st.text_input("الاسم الكريم")
        phone = st.text_input("رقم الهاتف")
        insta = st.text_input("حساب الإنستغرام (اختياري)")
        submit = st.form_submit_button("إرسال الطلب (تليجرام)")
        
        if submit:
            if name and phone:
                token = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
                chat_id = "7055252264"
                msg = f"🛒 طلب جديد!\nالاسم: {name}\nالهاتف: {phone}\nإنستغرام: {insta if insta else 'غير مذكور'}\nالسعر: {st.session_state.price}"
                
                res = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": msg})
                
                if res.status_code == 200:
                    st.balloons()
                    st.success("تم إرسال طلبك بنجاح!")
            else:
                st.error("يرجى ملء الاسم ورقم الهاتف!")
    st.markdown("</div>", unsafe_allow_html=True)
