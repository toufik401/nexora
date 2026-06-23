import streamlit as st
import requests
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexora Service</title>
    
    <!-- خط الكوفي العربي -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Reem_Kufi:wght@500;700&display=swap" rel="stylesheet">
    
    <!-- مكتبة التأثيرات البصرية (النجوم والخيوط الملونة) -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

    <style>
        /* المتغيرات الأساسية التي يمكن التحكم بها */
        :root {
            --main-bg: #0f172a;
            --main-color: #3b82f6;
            --text-color: #ffffff;
        }

        body {
            font-family: 'Reem Kufi', sans-serif;
            background-color: var(--main-bg);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            transition: all 0.3s ease;
        }

        /* حاوية الموقع الرئيسية */
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }

        /* العنوان بالخط الكوفي عريض وأبيض */
        .kufi-title {
            font-family: 'Reem Kufi', sans-serif;
            font-size: 2rem;
            font-weight: 700;
            color: #ffffff;
            margin-top: 20px;
            margin-bottom: 10px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.5);
        }

        /* واجهة الصورة - متجاوبة تماماً مع الهاتف والكمبيوتر */
        .hero-image-container {
            width: 100%;
            max-height: 300px;
            border-radius: 15px;
            overflow: hidden;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }

        .hero-image {
            width: 100%;
            height: 100%;
            object-fit: cover; /* يضمن عدم تشوه الصورة على الهاتف */
            display: block;
        }

        /* تصميم استمارة الطلب */
        .order-form {
            background: rgba(255, 255, 255, 0.05);
            padding: 25px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: right;
        }

        .form-group {
            margin-bottom: 18px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.95rem;
            color: #e2e8f0;
        }

        .form-group input, .form-group select {
            width: 100%;
            padding: 12px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            background: rgba(15, 23, 42, 0.6);
            color: #fff;
            font-family: inherit;
            font-size: 1rem;
            box-sizing: border-box;
            outline: none;
        }

        .form-group input:focus, .form-group select:focus {
            border-color: var(--main-color);
            box-shadow: 0 0 8px var(--main-color);
        }

        .submit-btn {
            width: 100%;
            padding: 14px;
            background-color: var(--main-color);
            color: white;
            border: none;
            border-radius: 8px;
            font-family: inherit;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
            margin-top: 10px;
        }

        .submit-btn:hover {
            opacity: 0.9;
        }

        /* --------- لوحة تحكم المالك (مخفية في الأسفل) --------- */
        .admin-panel {
            background: #1e293b;
            border: 2px dashed #ef4444;
            padding: 20px;
            margin-top: 50px;
            border-radius: 15px;
            text-align: right;
            color: #fff;
        }

        .admin-panel h3 {
            color: #ef4444;
            margin-top: 0;
            text-align: center;
        }

        /* رسالة النجاح */
        .success-msg {
            display: none;
            background: #10b981;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-weight: bold;
        }
    </style>
</head>
<body>

<div class="container">
    
    <!-- قسم الواجهة والصورة -->
    <div class="hero-image-container">
        <img id="view-image" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=500" alt="Nexora Header" class="hero-image">
    </div>

    <!-- العنوان بالخط الكوفي الأبيض -->
    <h1 id="view-title" class="kufi-title">مرحبا بيك في خدمت nexora</h1>
    <p style="color: #94a3b8; margin-bottom: 25px;">أدخل بياناتك لطلب متجرك الإلكتروني الاحترافي</p>

    <!-- استمارة الطلب للزبائن -->
    <form id="customerForm" class="order-form">
        <div class="form-group">
            <label for="fullName">الاسم الكامل:</label>
            <input type="text" id="fullName" required placeholder="أدخل اسمك الكامل">
        </div>

        <div class="form-group">
            <label for="province">الولاية:</label>
            <select id="province" required>
                <option value="" disabled selected>اختر ولايتك</option>
                <!-- يمكنك إضافة بقية الولايات هنا -->
                <option value="الجزائر">الجزائر</option>
                <option value="افلو">افلو</option>
                <option value="قسنطينة">قسنطينة</option>
                <option value="الأغواط">الأغواط</option>
                <option value="ورقلة">ورقلة</option>
                <option value="سطيف">سطيف</option>
            </select>
        </div>

        <div class="form-group">
            <label for="phone">رقم الهاتف:</label>
            <input type="tel" id="phone" required placeholder="06xxxxxxxx أو 05xxxxxxxx">
        </div>

        <div class="form-group">
            <label for="instagram">حساب أو رابط الانستغرام (لأخذ تفاصيل أكثر):</label>
            <input type="text" id="instagram" required placeholder="@username أو رابط الحساب">
        </div>

        <button type="submit" class="submit-btn">تأكيد إرسال الطلب ✨</button>
        <div id="successMessage" class="success-msg">تم إرسال طلبك بنجاح! سنتواصل معك قريباً.</div>
    </form>

    <br><hr style="border: 1px dashed rgba(255,255,255,0.1);"><br>

    <!-- 🔐 لوحة تحكم المالك (تظهر لك فقط لتغيير الإعدادات) -->
    <div class="admin-panel">
        <h3>🔐 لوحة تحكم المالك (Nexora Admin)</h3>
        <p style="font-size: 13px; color: #94a3b8; text-align: center;">(هذا القسم مخصص لك فقط لتعديل الواجهة مباشرة ولن يؤثر على طلبات الزبائن)</p>
        
        <div class="form-group">
            <label>تغيير عنوان الصفحة (خط كوفي):</label>
            <input type="text" id="input-title" value="مرحبا بيك في خدمت nexora" oninput="updateSettings()">
        </div>

        <div class="form-group">
            <label>رابط صورة الواجهة (URL):</label>
            <input type="text" id="input-image" value="https://i.ibb.co/v413XTWG/1782140096443.pn"updateSettings()">
        </div>

        <div class="form-group">
            <label>تغيير لون الهوية (الزر والحدود):</label>
            <input type="color" id="input-color" value="#3b82f6" onchange="updateSettings()">
        </div>
        
        <div class="form-group">
            <label>لون خلفية الموقع:</label>
            <input type="color" id="input-bg" value="#0f172a" onchange="updateSettings()">
        </div>
    </div>

</div>

<script>
    // ⚠️ إعدادات بوت تليجرام الخاص بك (املاًها هنا)
    const TELEGRAM_BOT_TOKEN = '8640762406:AAF540rnfipL54HSUIRZqODSsBcQjM2uybo'; 
    const TELEGRAM_CHAT_ID = '7055252264';

    // دالة لتحديث ألوان وعناوين الصفحة فوراً من لوحة التحكم
    function updateSettings() {
        const newTitle = document.getElementById('input-title').value;
        const newImg = document.getElementById('input-image').value;
        const newColor = document.getElementById('input-color').value;
        const newBg = document.getElementById('input-bg').value;

        // تطبيق التغييرات على الواجهة فوراً للزوار
        document.getElementById('view-title').innerText = newTitle;
        document.getElementById('view-image').src = newImg;
        document.documentElement.style.setProperty('--main-color', newColor);
        document.documentElement.style.setProperty('--main-bg', newBg);
    }

    // إرسال البيانات لبوت التليجرام وتشغيل الأنيميشن
    document.getElementById('customerForm').addEventListener('submit', function(e) {
        e.preventDefault();

        // جلب بيانات الزبون
        const name = document.getElementById('fullName').value;
        const province = document.getElementById('province').value;
        const phone = document.getElementById('phone').value;
        const instagram = document.getElementById('instagram').value;

        // تجهيز نص الرسالة للتليجرام
        const telegramMessage = `🚀 *طلب جديد لمتجر Nexora* 🚀\n\n` +
                                `👤 *الاسم:* ${name}\n` +
                                `📍 *الولاية:* ${province}\n` +
                                `📞 *الهاتف:* ${phone}\n` +
                                `📸 *الانستغرام:* ${instagram}`;

        // إرسال الطلب إلى تليجرام عبر الـ API
        const url = `https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage`;
        
        fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chat_id: TELEGRAM_CHAT_ID,
                text: telegramMessage,
                parse_mode: 'Markdown'
            })
        })
        .then(response => {
            if(response.ok) {
                // 1. إظهار رسالة النجاح
                document.getElementById('successMessage').style.display = 'block';
                
                // 2. إطلاق تأثير النجوم الذهبية والخيوط الملونة (Confetti)
                triggerCelebration();

                // إعادة تعيين الاستمارة
                document.getElementById('customerForm').reset();
            } else {
                alert('حدث خطأ أثناء إرسال الطلب، يرجى التحقق من إعدادات البوت.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('فشل الاتصال بالخادم.');
        });
    });

    // دالة الأنيميشن (نجوم وخيوط ملونة مبهجة)
    function triggerCelebration() {
        // الخيوط والأوراق الملونة تخرج من الجوانب
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.6 }
        });

        // النجوم الذهبية
        var duration = 2 * 1000;
        var end = Date.now() + duration;

        (function frame() {
            confetti({
                particleCount: 5,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: ['#ffd700', '#ffa500'] // ألوان ذهبية وبرتقالية
            });
            confetti({
                particleCount: 5,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: ['#ffd700', '#ffa500']
            });

            if (Date.now() < end) {
                requestAnimationFrame(frame);
            }
        }());
    }
</script>

</body>
</html>
