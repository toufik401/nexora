import streamlit as st
import requests

# 1. إعداد الصفحة
st.set_page_config(page_title="Nexora Store", layout="centered")

# 2. تنسيق CSS المحدث مع وضع الصورة كخلفية
st.markdown("""
    <style>
    /* إضافة الصورة كخلفية للمتجر (استخدام الرابط المباشر الخاص بك) */
    .stApp {
        background-image: url('https://i.ibb.co/v413XTWG/1782140096443.png');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* جعل نصوص التسميات (Labels) بيضاء وكبيرة */
    label {
        color: white !important;
        font-size: 24px !important;
        font-weight: bold !important;
    }
    
    /* تنسيق خانات الإدخال السوداء والخط أبيض */
    .stTextInput > div > div > input {
        background-color: black !important;
        color: white !important;
        border: 2px solid white !important;
        font-size: 18px !important;
        border-radius: 8px;
    }
    
    /* تنسيق العنوان العربي الكبير والمزخرف */
    .title-text {
        font-size: 65px !important;
        color: white !important;
        text-align: center;
        text-shadow: 4px 4px 8px #000000;
        font-weight: bold;
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
    }
    
    /* تنسيق زر الإرسال ليكون كبيراً وواضحاً */
    .stButton > button {
        width: 100% !important;
        background-color: white !important;
        color: black !important;
        font-size: 20px !important;
        font-weight: bold !important;
        padding: 10px !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان بالعربية
st.markdown('<p class="title-text">✨ متجر Nexora ✨</p>', unsafe_allow_html=True)

# 4. الحقول (الآن ستظهر النصوص بيضاء وكبيرة فوق خانات سوداء)
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الهاتف")
insta = st.text_input("حساب الانستغرام")

# 5. وظيفة إرسال الطلبية للبوت (ضع بياناتك هنا لتصلك الرسالة)
def send_to_telegram(message):
    # لا تنسى وضع التوكن الخاص بك والـ chat_id
    token = "8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo"
    chat_id = "7055252264"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    try:
        requests.get(url)
    except:
        st.error("حدث خطأ في الاتصال بالبوت.")

# 6. زر الإرسال
if st.button("إرسال الطلب"):
    if name and phone:
        # تنسيق الرسالة التي ستصلك للبوت
        msg = f"📦 طلب جديد من متجر Nexora:\n\nالاسم: {name}\nالهاتف: {phone}\nالانستغرام: {insta}"
        send_to_telegram(msg)
        st.success("تم إرسال طلبك بنجاح! 🎉")
        st.balloons()
    else:
        st.error("يرجى ملء الاسم ورقم الهاتف على الأقل.")
