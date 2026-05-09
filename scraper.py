#!/usr/bin/env python3
"""
🌟 كواغد - سوق الأغراض المستعملة
Ultra Premium Glass Morphism Design with Admin Protection
"""

import os
import json
import base64

def create_directory_structure():
    directories = ['css', 'js', 'images', 'assets']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ تم إنشاء مجلد: {directory}")

def create_index_html():
    html = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>كواغد | سوق الأغراض المستعملة</title>
    <meta name="description" content="سوق كواغد - أفضل وجهة لبيع وشراء الأغراض المستعملة بتصميم زجاجي عصري">
    <link rel="stylesheet" href="css/glass-morphism.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/bubbles.css">
    <link rel="stylesheet" href="css/admin.css">
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=Playfair+Display:wght@400;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
    <div class="bubbles-container">
        <div class="bubble bubble-1"></div><div class="bubble bubble-2"></div><div class="bubble bubble-3"></div>
        <div class="bubble bubble-4"></div><div class="bubble bubble-5"></div><div class="bubble bubble-6"></div>
        <div class="bubble bubble-7"></div><div class="bubble bubble-8"></div><div class="bubble bubble-9"></div>
        <div class="bubble bubble-10"></div>
    </div>
    <div class="particles" id="particles"></div>

    <nav class="glass-nav">
        <div class="nav-container">
            <div class="logo-section">
                <div class="logo-icon"><i class="fas fa-recycle"></i></div>
                <span class="logo-text">كواغد</span>
            </div>
            <div class="nav-links">
                <a href="#home" class="nav-link active">الرئيسية</a>
                <a href="#products" class="nav-link">المنتجات</a>
                <a href="#sell" class="nav-link">بيع منتجك</a>
                <a href="#about" class="nav-link">من نحن</a>
                <a href="#contact" class="nav-link">اتصل بنا</a>
                <div class="cart-icon-wrapper" onclick="toggleCart()">
                    <div class="cart-icon"><i class="fas fa-shopping-bag"></i><span class="cart-badge" id="cartCount">0</span></div>
                </div>
            </div>
        </div>
    </nav>

    <section id="home" class="hero-section">
        <div class="hero-content">
            <div class="glass-card hero-card">
                <span class="premium-badge">✨ اشتري وبيع بذكاء</span>
                <h1 class="hero-title">أهلاً بك في<br><span class="gold-text">سوق كواغد</span></h1>
                <p class="hero-description">وجهتك الأولى لشراء وبيع الأغراض المستعملة. منصة آمنة وسهلة للعثور على أفضل الصفقات أو بيع أغراضك بأفضل الأسعار.</p>
                <div class="hero-actions">
                    <button class="glass-btn primary-btn" onclick="scrollToSection('products')"><i class="fas fa-search"></i> تصفح المنتجات</button>
                    <button class="glass-btn secondary-btn" onclick="scrollToSection('sell')"><i class="fas fa-tag"></i> اعرض منتجك للبيع</button>
                </div>
            </div>
        </div>
    </section>

    <section class="features-section">
        <div class="features-grid">
            <div class="glass-card feature-card"><div class="feature-icon"><i class="fas fa-hand-holding-usd"></i></div><h3>أسعار تنافسية</h3><p>أفضل الأسعار للأغراض المستعملة بحالة ممتازة</p></div>
            <div class="glass-card feature-card"><div class="feature-icon"><i class="fas fa-shield-alt"></i></div><h3>تعامل آمن</h3><p>نظام تقييم للبائعين والمشترين لضمان المصداقية</p></div>
            <div class="glass-card feature-card"><div class="feature-icon"><i class="fas fa-box-open"></i></div><h3>منتجات متنوعة</h3><p>آلاف المنتجات المستعملة في مكان واحد</p></div>
            <div class="glass-card feature-card"><div class="feature-icon"><i class="fas fa-headset"></i></div><h3>دعم متواصل</h3><p>فريق دعم جاهز لمساعدتك في أي وقت</p></div>
        </div>
    </section>

    <section id="sell" class="sell-section">
        <div class="section-header"><span class="section-badge">بيع منتجك</span><h2 class="section-title">اعرض <span class="gold-text">أغراضك</span> للبيع</h2><p class="section-description">املأ النموذج التالي لعرض منتجك المستعمل في سوق كواغد</p></div>
        <form class="glass-card sell-form" id="sellForm">
            <div class="form-section"><h3><i class="fas fa-image"></i> صورة المنتج</h3>
                <div class="upload-glass" id="uploadAreaSell">
                    <input type="file" id="imageUploadSell" accept="image/*" hidden onchange="handleSellImageUpload(event)">
                    <div class="upload-content"><i class="fas fa-cloud-upload-alt upload-main-icon"></i><p>اسحب وأفلت الصورة هنا</p><span class="upload-divider">أو</span><button type="button" class="glass-btn secondary-btn" onclick="document.getElementById('imageUploadSell').click()"><i class="fas fa-folder-open"></i> اختر صورة</button></div>
                </div>
                <div id="uploadProgressSell" class="upload-progress"></div><div id="imagePreviewSell" class="image-preview-glass"></div><input type="hidden" id="sellProductImage">
            </div>
            <div class="form-row">
                <div class="input-glass"><i class="fas fa-tag"></i><input type="text" id="sellProductName" placeholder="اسم المنتج" required></div>
                <div class="input-glass"><i class="fas fa-dollar-sign"></i><input type="number" id="sellProductPrice" placeholder="السعر ($)" required step="0.01"></div>
            </div>
            <div class="input-glass"><i class="fas fa-layer-group"></i><select id="sellProductCategory" required><option value="">اختر التصنيف...</option><option value="electronics">📱 إلكترونيات</option><option value="furniture">🪑 أثاث</option><option value="clothing">👕 ملابس</option><option value="books">📚 كتب</option><option value="sports">⚽ رياضة</option><option value="toys">🧸 ألعاب</option><option value="other">📦 أخرى</option></select></div>
            <div class="input-glass"><i class="fas fa-info-circle"></i><select id="sellProductCondition" required><option value="">حالة المنتج...</option><option value="like-new">مثل الجديد</option><option value="excellent">ممتاز</option><option value="good">جيد</option><option value="fair">مقبول</option></select></div>
            <div class="input-glass"><i class="fas fa-align-left"></i><textarea id="sellProductDescription" placeholder="وصف المنتج وحالته..." rows="4" required></textarea></div>
            <div class="input-glass"><i class="fas fa-map-marker-alt"></i><input type="text" id="sellProductLocation" placeholder="موقع المنتج (المدينة)" required></div>
            <div class="input-glass"><i class="fas fa-phone"></i><input type="tel" id="sellProductPhone" placeholder="رقم التواصل (اختياري)"></div>
            <button type="submit" class="glass-btn primary-btn full-width"><i class="fas fa-plus-circle"></i> أضف المنتج للسوق</button>
        </form>
    </section>

    <section id="products" class="products-section">
        <div class="section-header"><span class="section-badge">المنتجات</span><h2 class="section-title">أغراض <span class="gold-text">مستعملة</span> للبيع</h2><p class="section-description">تصفح أحدث العروض في سوق كواغد</p></div>
        <div class="filter-buttons">
            <button class="filter-btn active" onclick="filterProducts('all')"><i class="fas fa-th-large"></i> الكل</button>
            <button class="filter-btn" onclick="filterProducts('electronics')"><i class="fas fa-mobile-alt"></i> إلكترونيات</button>
            <button class="filter-btn" onclick="filterProducts('furniture')"><i class="fas fa-couch"></i> أثاث</button>
            <button class="filter-btn" onclick="filterProducts('clothing')"><i class="fas fa-tshirt"></i> ملابس</button>
            <button class="filter-btn" onclick="filterProducts('books')"><i class="fas fa-book"></i> كتب</button>
            <button class="filter-btn" onclick="filterProducts('sports')"><i class="fas fa-futbol"></i> رياضة</button>
            <button class="filter-btn" onclick="filterProducts('toys')"><i class="fas fa-puzzle-piece"></i> ألعاب</button>
            <button class="filter-btn" onclick="filterProducts('other')"><i class="fas fa-box"></i> أخرى</button>
        </div>
        <div class="products-grid" id="productsGrid"></div>
    </section>

    <section id="about" class="about-section">
        <div class="about-content">
            <div class="about-text"><span class="section-badge">من نحن</span><h2>قصة <span class="gold-text">كواغد</span></h2><p>كواغد هو سوق متكامل لبيع وشراء الأغراض المستعملة. نؤمن بأن كل غرض مستعمل له قيمة ويمكن أن يكون كنزاً لشخص آخر.</p><p>هدفنا تعزيز ثقافة إعادة الاستخدام وتقليل الهدر مع توفير فرص رائعة للجميع.</p>
                <div class="stats-grid"><div class="glass-card stat-card"><span class="stat-number">+5000</span><span class="stat-label">منتج معروض</span></div><div class="glass-card stat-card"><span class="stat-number">+2000</span><span class="stat-label">بائع نشط</span></div><div class="glass-card stat-card"><span class="stat-number">+1500</span><span class="stat-label">صفقة ناجحة</span></div></div>
            </div>
            <div class="about-image"><div class="glass-card image-frame"><div class="frame-content"><i class="fas fa-recycle"></i><span>كواغد<br>للغرض</span></div></div></div>
        </div>
    </section>

    <section id="contact" class="contact-section">
        <div class="section-header"><span class="section-badge">اتصل بنا</span><h2 class="section-title">تواصل <span class="gold-text">معنا</span></h2></div>
        <form class="glass-card contact-form" id="contactForm">
            <div class="form-row"><div class="input-group"><i class="fas fa-user"></i><input type="text" placeholder="الاسم الكامل" required></div><div class="input-group"><i class="fas fa-envelope"></i><input type="email" placeholder="البريد الإلكتروني" required></div></div>
            <div class="input-group"><i class="fas fa-comment"></i><textarea placeholder="رسالتك..." rows="5" required></textarea></div>
            <button type="submit" class="glass-btn primary-btn"><i class="fas fa-paper-plane"></i> إرسال الرسالة</button>
        </form>
    </section>

    <button class="admin-trigger" onclick="showAdminLock()" title="لوحة التحكم"><i class="fas fa-lock"></i></button>
    <div id="adminLockModal" class="modal glass-modal">
        <div class="glass-card lock-card">
            <div class="lock-header"><div class="lock-icon"><i class="fas fa-shield-halved"></i></div><h2>لوحة التحكم</h2><p>أدخل رمز الدخول للمتابعة</p></div>
            <div class="pin-input-container"><div class="pin-inputs"><input type="password" maxlength="1" class="pin-input" id="pin1" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)"><input type="password" maxlength="1" class="pin-input" id="pin2" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)"><input type="password" maxlength="1" class="pin-input" id="pin3" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)"><input type="password" maxlength="1" class="pin-input" id="pin4" oninput="pinInput(this)" onkeydown="handlePinKey(event, this)"></div><div id="pinError" class="pin-error"></div></div>
            <div class="lock-actions"><button class="glass-btn secondary-btn" onclick="closeAdminLock()"><i class="fas fa-times"></i> إلغاء</button><button class="glass-btn primary-btn" onclick="verifyPin()"><i class="fas fa-arrow-right"></i> دخول</button></div>
        </div>
    </div>

    <div id="adminPanel" class="admin-panel glass-panel">
        <div class="panel-header"><div class="panel-title"><i class="fas fa-crown"></i><h2>إدارة منتجات كواغد</h2></div><button class="close-panel" onclick="closeAdminPanel()"><i class="fas fa-times"></i></button></div>
        <form id="productForm" class="admin-form">
            <div class="form-section"><h3><i class="fas fa-image"></i> صورة المنتج</h3><div class="upload-glass" id="uploadArea"><input type="file" id="imageUpload" accept="image/*" hidden onchange="handleImageUpload(event)"><div class="upload-content"><i class="fas fa-cloud-upload-alt upload-main-icon"></i><p>اسحب وأفلت الصورة هنا</p><span class="upload-divider">أو</span><button type="button" class="glass-btn secondary-btn" onclick="document.getElementById('imageUpload').click()"><i class="fas fa-folder-open"></i> اختر صورة</button></div></div><div id="uploadProgress" class="upload-progress"></div><div id="imagePreview" class="image-preview-glass"></div><input type="hidden" id="productImage"></div>
            <div class="form-section"><h3><i class="fas fa-info-circle"></i> تفاصيل المنتج</h3>
                <div class="input-glass"><i class="fas fa-tag"></i><input type="text" id="productName" placeholder="اسم المنتج" required></div>
                <div class="input-glass"><i class="fas fa-dollar-sign"></i><input type="number" id="productPrice" placeholder="السعر ($)" required step="0.01"></div>
                <div class="input-glass"><i class="fas fa-layer-group"></i><select id="productCategory" required><option value="">اختر التصنيف...</option><option value="electronics">📱 إلكترونيات</option><option value="furniture">🪑 أثاث</option><option value="clothing">👕 ملابس</option><option value="books">📚 كتب</option><option value="sports">⚽ رياضة</option><option value="toys">🧸 ألعاب</option><option value="other">📦 أخرى</option></select></div>
                <div class="input-glass"><i class="fas fa-check-circle"></i><select id="productCondition" required><option value="">حالة المنتج...</option><option value="like-new">مثل الجديد</option><option value="excellent">ممتاز</option><option value="good">جيد</option><option value="fair">مقبول</option></select></div>
                <div class="input-glass"><i class="fas fa-align-left"></i><textarea id="productDescription" placeholder="وصف المنتج..." rows="4" required></textarea></div>
            </div>
            <div class="form-actions"><button type="submit" class="glass-btn primary-btn"><i class="fas fa-plus-circle"></i> إضافة المنتج</button><button type="button" class="glass-btn secondary-btn" onclick="resetAdminForm()"><i class="fas fa-redo"></i> مسح النموذج</button></div>
        </form>
    </div>

    <div id="cartModal" class="modal glass-modal">
        <div class="glass-card cart-card">
            <div class="cart-header"><h2><i class="fas fa-shopping-bag"></i> سلة التسوق</h2><button class="close-cart" onclick="toggleCart()"><i class="fas fa-times"></i></button></div>
            <div id="cartItems" class="cart-items"><div class="empty-cart-state"><i class="fas fa-shopping-bag"></i><p>سلة التسوق فارغة</p><span>ابدأ التسوق وأضف منتجاتك المفضلة</span></div></div>
            <div class="cart-footer"><div class="cart-total"><span>المجموع:</span><span id="cartTotal" class="total-price">$0.00</span></div><button class="glass-btn primary-btn full-width" onclick="checkout()"><i class="fas fa-credit-card"></i> إتمام الشراء</button></div>
        </div>
    </div>

    <footer class="glass-footer">
        <div class="footer-content">
            <div class="footer-brand"><i class="fas fa-recycle"></i><h3>كواغد</h3><p>سوق الأغراض المستعملة الأول</p></div>
            <div class="footer-links"><h4>روابط سريعة</h4><a href="#home">الرئيسية</a><a href="#products">المنتجات</a><a href="#sell">بيع منتجك</a><a href="#about">من نحن</a><a href="#contact">اتصل بنا</a></div>
            <div class="footer-contact"><h4>تواصل معنا</h4><p><i class="fas fa-envelope"></i> info@kwaged.com</p><p><i class="fas fa-phone"></i> +1 234 567 8900</p><div class="social-icons"><a href="#" class="social-icon"><i class="fab fa-instagram"></i></a><a href="#" class="social-icon"><i class="fab fa-twitter"></i></a><a href="#" class="social-icon"><i class="fab fa-whatsapp"></i></a></div></div>
        </div>
        <div class="footer-bottom"><p>© 2024 كواغد - جميع الحقوق محفوظة</p></div>
    </footer>

    <div id="toastContainer" class="toast-container"></div>
    <script src="js/products.js"></script><script src="js/admin.js"></script><script src="js/app.js"></script>
</body>
</html>'''
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✅ تم إنشاء: index.html")

def create_glass_morphism_css():
    css = '''/* GLASS MORPHISM DESIGN SYSTEM - كواغد */
:root {
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    --glass-blur: blur(20px);
    --gold: #4CAF50;
    --gold-light: #A5D6A7;
    --gold-dark: #2E7D32;
    --gold-gradient: linear-gradient(135deg, #4CAF50 0%, #81C784 50%, #2E7D32 100%);
    --bg-primary: #0a0a0a;
    --bg-secondary: #1a1a1a;
    --text-primary: #ffffff;
    --text-secondary: rgba(255, 255, 255, 0.7);
    --text-gold: #4CAF50;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    font-family: 'Cairo', sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    overflow-x: hidden;
    min-height: 100vh;
    position: relative;
}
.glass-card {
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    box-shadow: var(--glass-shadow);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.glass-card:hover {
    border-color: rgba(76, 175, 80, 0.3);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2), 0 0 40px rgba(76, 175, 80, 0.1);
    transform: translateY(-2px);
}
.glass-btn {
    padding: 1rem 2rem;
    border-radius: 50px;
    font-weight: 700;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 1px solid var(--glass-border);
    font-family: 'Cairo', sans-serif;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    text-decoration: none;
}
.glass-btn.primary-btn {
    background: var(--gold-gradient);
    color: #000;
    border: none;
    box-shadow: 0 8px 32px rgba(76, 175, 80, 0.3);
}
.glass-btn.primary-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(76, 175, 80, 0.5);
}
.glass-btn.secondary-btn {
    background: rgba(255, 255, 255, 0.05);
    color: var(--text-primary);
}
.glass-btn.secondary-btn:hover {
    background: rgba(255, 255, 255, 0.1);
    border-color: rgba(76, 175, 80, 0.5);
}
.glass-nav {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 90%;
    max-width: 1200px;
    background: var(--glass-bg);
    backdrop-filter: blur(30px);
    -webkit-backdrop-filter: blur(30px);
    border: 1px solid var(--glass-border);
    border-radius: 50px;
    padding: 1rem 2rem;
    z-index: 1000;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    transition: all 0.3s ease;
}
.glass-nav.scrolled {
    top: 10px;
    background: rgba(10, 10, 10, 0.8);
}
.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.logo-section {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.logo-icon {
    width: 45px;
    height: 45px;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #000;
    font-size: 1.3rem;
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
    animation: logoGlow 3s ease-in-out infinite;
}
@keyframes logoGlow {
    0%, 100% { box-shadow: 0 0 20px rgba(76, 175, 80, 0.3); }
    50% { box-shadow: 0 0 40px rgba(76, 175, 80, 0.6); }
}
.logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 900;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 2px;
}
.nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
}
.nav-link {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    position: relative;
    padding: 0.5rem 0;
}
.nav-link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gold-gradient);
    transition: width 0.3s ease;
}
.nav-link:hover, .nav-link.active {
    color: var(--text-primary);
}
.nav-link:hover::after, .nav-link.active::after {
    width: 100%;
}
.cart-icon-wrapper {
    position: relative;
    cursor: pointer;
}
.cart-icon {
    width: 45px;
    height: 45px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid var(--glass-border);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    transition: all 0.3s ease;
}
.cart-icon:hover {
    background: rgba(76, 175, 80, 0.2);
    border-color: rgba(76, 175, 80, 0.5);
}
.cart-badge {
    position: absolute;
    top: -5px;
    right: -5px;
    width: 22px;
    height: 22px;
    background: var(--gold-gradient);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: bold;
    color: #000;
}
.gold-text {
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}
::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.05); }
::-webkit-scrollbar-thumb { background: var(--gold-gradient); border-radius: 10px; }
'''
    with open('css/glass-morphism.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/glass-morphism.css")

def create_bubbles_css():
    css = '''.bubbles-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; overflow: hidden; }
.bubble { position: absolute; border-radius: 50%; background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.1), rgba(76,175,80,0.05), transparent 70%); border: 1px solid rgba(255,255,255,0.05); backdrop-filter: blur(5px); animation: floatBubble linear infinite; }
.bubble-1 { width: 150px; height: 150px; left: 10%; animation-duration: 15s; animation-delay: 0s; }
.bubble-2 { width: 100px; height: 100px; left: 25%; animation-duration: 18s; animation-delay: 2s; }
.bubble-3 { width: 200px; height: 200px; left: 40%; animation-duration: 20s; animation-delay: 4s; }
.bubble-4 { width: 120px; height: 120px; left: 55%; animation-duration: 16s; animation-delay: 1s; }
.bubble-5 { width: 80px; height: 80px; left: 70%; animation-duration: 22s; animation-delay: 3s; }
.bubble-6 { width: 180px; height: 180px; left: 85%; animation-duration: 19s; animation-delay: 5s; }
.bubble-7 { width: 90px; height: 90px; left: 15%; animation-duration: 17s; animation-delay: 2.5s; }
.bubble-8 { width: 160px; height: 160px; left: 50%; animation-duration: 21s; animation-delay: 1.5s; }
.bubble-9 { width: 110px; height: 110px; left: 75%; animation-duration: 23s; animation-delay: 3.5s; }
.bubble-10 { width: 140px; height: 140px; left: 35%; animation-duration: 24s; animation-delay: 4.5s; }
@keyframes floatBubble {
    0% { transform: translateY(100vh) scale(0); opacity: 0; }
    10% { opacity: 0.8; }
    50% { transform: translateY(50vh) translateX(50px) scale(1); opacity: 0.6; }
    90% { opacity: 0.2; }
    100% { transform: translateY(-20vh) translateX(-50px) scale(0.5); opacity: 0; }
}
.particles { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
.particle { position: absolute; width: 4px; height: 4px; background: var(--gold); border-radius: 50%; animation: particleFloat linear infinite; box-shadow: 0 0 10px rgba(76,175,80,0.5); }
@keyframes particleFloat {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
    10% { opacity: 1; }
    90% { opacity: 0.5; }
    100% { transform: translateY(-20vh) rotate(720deg); opacity: 0; }
}'''
    with open('css/bubbles.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/bubbles.css")

def create_style_css():
    css = '''.hero-section { min-height: 100vh; display: flex; align-items: center; justify-content: center; padding: 2rem; position: relative; z-index: 1; }
.hero-card { max-width: 700px; padding: 4rem; text-align: center; animation: fadeInUp 1s ease; }
.premium-badge { display: inline-block; padding: 0.5rem 2rem; background: rgba(76,175,80,0.15); border: 1px solid rgba(76,175,80,0.3); border-radius: 50px; color: var(--gold); font-weight: 600; margin-bottom: 2rem; }
.hero-title { font-family: 'Playfair Display', serif; font-size: 4rem; margin-bottom: 1.5rem; line-height: 1.3; }
.hero-description { color: var(--text-secondary); font-size: 1.2rem; margin-bottom: 2.5rem; line-height: 1.8; }
.hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.features-section { padding: 5rem 2rem; position: relative; z-index: 1; }
.features-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
.feature-card { padding: 2.5rem; text-align: center; }
.feature-icon { width: 70px; height: 70px; margin: 0 auto 1.5rem; background: var(--gold-gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.8rem; color: #000; }
.sell-section { padding: 5rem 2rem; position: relative; z-index: 1; }
.sell-form { max-width: 700px; margin: 0 auto; padding: 2rem; }
.products-section { padding: 5rem 2rem; position: relative; z-index: 1; }
.section-header { text-align: center; margin-bottom: 3rem; }
.section-badge { display: inline-block; padding: 0.5rem 1.5rem; background: rgba(76,175,80,0.1); border: 1px solid rgba(76,175,80,0.2); border-radius: 50px; color: var(--gold); font-weight: 600; margin-bottom: 1rem; }
.section-title { font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 1rem; }
.section-description { color: var(--text-secondary); font-size: 1.1rem; }
.filter-buttons { display: flex; justify-content: center; gap: 0.5rem; margin-bottom: 3rem; flex-wrap: wrap; }
.filter-btn { padding: 0.7rem 1.2rem; border-radius: 50px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-secondary); cursor: pointer; transition: all 0.3s ease; font-family: 'Cairo', sans-serif; display: flex; align-items: center; gap: 0.5rem; backdrop-filter: blur(10px); font-size: 0.85rem; }
.filter-btn.active, .filter-btn:hover { background: var(--gold-gradient); color: #000; border-color: transparent; }
.products-grid { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 2rem; }
.product-card { position: relative; overflow: hidden; }
.product-badge { position: absolute; top: 1rem; right: 1rem; padding: 0.3rem 1rem; background: var(--gold-gradient); color: #000; border-radius: 50px; font-size: 0.8rem; font-weight: 700; z-index: 2; }
.product-condition-badge { position: absolute; top: 1rem; left: 1rem; padding: 0.3rem 0.8rem; background: rgba(0,0,0,0.7); color: #fff; border-radius: 50px; font-size: 0.75rem; z-index: 2; backdrop-filter: blur(5px); }
.product-image-wrapper { position: relative; overflow: hidden; border-radius: 20px 20px 0 0; }
.product-image { width: 100%; height: 350px; object-fit: cover; transition: transform 0.6s ease; }
.product-card:hover .product-image { transform: scale(1.1); }
.product-info { padding: 1.5rem; }
.product-name { font-size: 1.5rem; color: var(--gold); margin-bottom: 0.5rem; }
.product-description { color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 0.5rem; }
.product-location { color: var(--text-secondary); font-size: 0.8rem; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 0.5rem; }
.product-price { font-size: 2rem; font-weight: 900; background: var(--gold-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 1rem; }
.product-actions { display: flex; gap: 0.5rem; }
.product-actions .glass-btn { flex: 1; padding: 0.8rem; font-size: 0.9rem; justify-content: center; }
.about-section { padding: 5rem 2rem; position: relative; z-index: 1; }
.about-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }
.stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 2rem; }
.stat-card { text-align: center; padding: 1.5rem; }
.stat-number { font-size: 1.8rem; font-weight: 900; background: var(--gold-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; display: block; }
.image-frame { height: 400px; display: flex; align-items: center; justify-content: center; }
.frame-content { text-align: center; font-size: 2rem; color: var(--gold); }
.frame-content i { font-size: 5rem; margin-bottom: 1rem; }
.contact-section { padding: 5rem 2rem; position: relative; z-index: 1; }
.contact-form { max-width: 600px; margin: 0 auto; padding: 3rem; }
.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem; }
.input-group { position: relative; margin-bottom: 1rem; }
.input-group i { position: absolute; right: 1rem; top: 50%; transform: translateY(-50%); color: var(--text-secondary); }
.input-group input, .input-group textarea { width: 100%; padding: 1rem 3rem 1rem 1rem; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); border-radius: 15px; color: var(--text-primary); font-family: 'Cairo', sans-serif; transition: all 0.3s ease; }
.input-group input:focus, .input-group textarea:focus { outline: none; border-color: var(--gold); box-shadow: 0 0 20px rgba(76,175,80,0.1); }
.glass-footer { background: var(--glass-bg); backdrop-filter: blur(20px); border-top: 1px solid var(--glass-border); padding: 4rem 2rem 2rem; position: relative; z-index: 1; }
.footer-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; }
.footer-brand i { font-size: 2rem; color: var(--gold); }
.footer-links a { display: block; color: var(--text-secondary); text-decoration: none; margin-bottom: 0.5rem; transition: color 0.3s ease; }
.footer-links a:hover { color: var(--gold); }
.social-icons { display: flex; gap: 1rem; margin-top: 1rem; }
.social-icon { width: 40px; height: 40px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: var(--text-secondary); transition: all 0.3s ease; text-decoration: none; }
.social-icon:hover { background: var(--gold-gradient); color: #000; border-color: transparent; }
.footer-bottom { text-align: center; padding-top: 2rem; margin-top: 2rem; border-top: 1px solid var(--glass-border); color: var(--text-secondary); }
.modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 2000; align-items: center; justify-content: center; }
.modal.active { display: flex; }
.toast-container { position: fixed; top: 20px; right: 20px; z-index: 3000; display: flex; flex-direction: column; gap: 0.5rem; }
.toast { padding: 1rem 2rem; background: var(--glass-bg); backdrop-filter: blur(20px); border: 1px solid var(--glass-border); border-radius: 15px; color: var(--text-primary); animation: slideInRight 0.3s ease; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
.toast.success { border-color: rgba(76,175,80,0.5); }
.toast.error { border-color: rgba(244,67,54,0.5); }
@keyframes slideInRight { from { transform: translateX(100%); opacity: 0; } to { transform: translateX(0); opacity: 1; } }
.full-width { width: 100%; justify-content: center; }
@media (max-width: 768px) {
    .hero-title { font-size: 2.5rem; }
    .about-content { grid-template-columns: 1fr; }
    .products-grid { grid-template-columns: 1fr; }
    .form-row { grid-template-columns: 1fr; }
    .glass-nav { width: 95%; padding: 0.8rem 1rem; border-radius: 30px; }
    .filter-btn { padding: 0.5rem 0.8rem; font-size: 0.75rem; }
}'''
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/style.css")

def create_admin_css():
    css = '''.admin-trigger { position: fixed; bottom: 30px; left: 30px; width: 60px; height: 60px; border-radius: 50%; background: var(--glass-bg); backdrop-filter: blur(20px); border: 2px solid var(--glass-border); color: var(--gold); font-size: 1.5rem; cursor: pointer; z-index: 999; transition: all 0.3s ease; box-shadow: 0 8px 32px rgba(0,0,0,0.2); }
.admin-trigger:hover { transform: scale(1.1); border-color: var(--gold); box-shadow: 0 0 30px rgba(76,175,80,0.3); }
.glass-modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); backdrop-filter: blur(10px); z-index: 2000; align-items: center; justify-content: center; }
.glass-modal.active { display: flex; }
.lock-card { width: 90%; max-width: 450px; padding: 3rem; text-align: center; animation: scaleIn 0.3s ease; }
@keyframes scaleIn { from { transform: scale(0.9); opacity: 0; } to { transform: scale(1); opacity: 1; } }
.lock-icon { width: 80px; height: 80px; margin: 0 auto 1.5rem; background: var(--gold-gradient); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; color: #000; box-shadow: 0 0 30px rgba(76,175,80,0.3); animation: pulse 2s ease-in-out infinite; }
@keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
.pin-inputs { display: flex; gap: 1rem; justify-content: center; margin-bottom: 1rem; }
.pin-input { width: 60px; height: 60px; text-align: center; font-size: 1.5rem; background: rgba(255,255,255,0.05); border: 2px solid var(--glass-border); border-radius: 15px; color: var(--text-primary); transition: all 0.3s ease; font-family: 'Cairo', sans-serif; }
.pin-input:focus { outline: none; border-color: var(--gold); box-shadow: 0 0 20px rgba(76,175,80,0.2); }
.pin-input.filled { background: rgba(76,175,80,0.1); border-color: var(--gold); }
.pin-error { color: #f44336; font-size: 0.9rem; min-height: 20px; }
.admin-panel { position: fixed; top: 0; left: -100%; width: 100%; max-width: 500px; height: 100vh; background: rgba(10,10,10,0.95); backdrop-filter: blur(30px); border-right: 1px solid var(--glass-border); z-index: 2001; transition: left 0.4s cubic-bezier(0.4,0,0.2,1); overflow-y: auto; }
.admin-panel.active { left: 0; }
.panel-header { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; border-bottom: 1px solid var(--glass-border); position: sticky; top: 0; background: rgba(10,10,10,0.95); backdrop-filter: blur(30px); z-index: 10; }
.panel-title { display: flex; align-items: center; gap: 0.5rem; color: var(--gold); }
.close-panel { width: 40px; height: 40px; border-radius: 50%; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-secondary); cursor: pointer; display: flex; align-items: center; justify-content: center; }
.form-section { margin-bottom: 2rem; padding: 1.5rem; background: rgba(255,255,255,0.02); border: 1px solid var(--glass-border); border-radius: 20px; }
.form-section h3 { margin-bottom: 1.5rem; color: var(--gold); display: flex; align-items: center; gap: 0.5rem; }
.upload-glass { border: 2px dashed rgba(255,255,255,0.1); border-radius: 20px; padding: 2rem; text-align: center; cursor: pointer; transition: all 0.3s ease; background: rgba(255,255,255,0.02); }
.upload-glass:hover, .upload-glass.highlight { border-color: var(--gold); background: rgba(76,175,80,0.05); }
.upload-main-icon { font-size: 3rem; color: var(--gold); margin-bottom: 1rem; }
.image-preview-glass { margin-top: 1rem; border-radius: 15px; overflow: hidden; border: 1px solid var(--glass-border); }
.image-preview-glass img { width: 100%; height: 200px; object-fit: cover; }
.input-glass { position: relative; margin-bottom: 1rem; }
.input-glass i { position: absolute; right: 1rem; top: 50%; transform: translateY(-50%); color: var(--text-secondary); z-index: 1; }
.input-glass input, .input-glass select, .input-glass textarea { width: 100%; padding: 1rem 3rem 1rem 1rem; background: rgba(255,255,255,0.03); border: 1px solid var(--glass-border); border-radius: 15px; color: var(--text-primary); font-family: 'Cairo', sans-serif; transition: all 0.3s ease; }
.input-glass select option { background: #1a1a1a; color: var(--text-primary); }
.input-glass input:focus, .input-glass select:focus, .input-glass textarea:focus { outline: none; border-color: var(--gold); box-shadow: 0 0 20px rgba(76,175,80,0.1); }
.form-actions { display: flex; gap: 1rem; margin-top: 2rem; }
.form-actions .glass-btn { flex: 1; justify-content: center; }
.cart-card { width: 90%; max-width: 500px; max-height: 80vh; overflow-y: auto; animation: scaleIn 0.3s ease; }
.cart-header { display: flex; justify-content: space-between; align-items: center; padding: 1.5rem; border-bottom: 1px solid var(--glass-border); }
.cart-header h2 { display: flex; align-items: center; gap: 0.5rem; color: var(--gold); }
.close-cart { width: 35px; height: 35px; border-radius: 50%; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-secondary); cursor: pointer; display: flex; align-items: center; justify-content: center; }
.cart-items { padding: 1.5rem; }
.empty-cart-state { text-align: center; padding: 3rem; color: var(--text-secondary); }
.empty-cart-state i { font-size: 4rem; color: var(--gold); margin-bottom: 1rem; opacity: 0.5; }
.cart-footer { padding: 1.5rem; border-top: 1px solid var(--glass-border); }
.cart-total { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; font-size: 1.2rem; }
.total-price { font-weight: 900; background: var(--gold-gradient); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }'''
    with open('css/admin.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ تم إنشاء: css/admin.css")

def create_products_js():
    js = '''const productsDB = [{id:1,name:"آيفون 12 برو - 256GB",price:450,category:"electronics",description:"جهاز آيفون 12 برو سعة 256GB بحالة ممتازة، مع الشاحن والكرتونة الأصلية.",condition:"excellent",location:"نيويورك",phone:"1234567890",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/iphone12",badge:"الأكثر طلباً"},{id:2,name:"طاولة طعام خشبية",price:180,category:"furniture",description:"طاولة طعام من الخشب الصلب تتسع لـ 6 أشخاص، بحالة جيدة جداً.",condition:"good",location:"لوس أنجلوس",phone:"9876543210",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/table",badge:""},{id:3,name:"مجموعة كتب برمجة",price:35,category:"books",description:"مجموعة من 5 كتب برمجة تشمل Python، JavaScript، React، Node.js، و SQL.",condition:"like-new",location:"شيكاغو",phone:"",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/books",badge:"صفقة ممتازة"},{id:4,name:"دراجة هوائية جبلية",price:220,category:"sports",description:"دراجة جبلية من ماركة Trek مقاس 29 بوصة، استخدمت لفترة قصيرة فقط.",condition:"excellent",location:"بوسطن",phone:"5551112233",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/bike",badge:""},{id:5,name:"بلاي ستيشن 5",price:380,category:"electronics",description:"جهاز بلاي ستيشن 5 مع يدين تحكم و 3 ألعاب. الجهاز بحالة ممتازة.",condition:"excellent",location:"ميامي",phone:"4445556667",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/ps5",badge:"جديد"},{id:6,name:"كنبة جلدية 3 مقاعد",price:280,category:"furniture",description:"كنبة جلدية لون بني غامق، 3 مقاعد. بحالة جيدة مع بعض علامات الاستخدام.",condition:"good",location:"دالاس",phone:"",image:"https://res.cloudinary.com/dmla61v7n/image/upload/v1/kwaged/sofa",badge:""}];
let products = JSON.parse(localStorage.getItem('kwagedProducts')) || productsDB;
let cart = JSON.parse(localStorage.getItem('kwagedCart')) || [];
function saveProducts() { localStorage.setItem('kwagedProducts', JSON.stringify(products)); }
function saveCart() { localStorage.setItem('kwagedCart', JSON.stringify(cart)); }
function getConditionText(c) { const conds = {'like-new':'مثل الجديد','excellent':'ممتاز','good':'جيد','fair':'مقبول'}; return conds[c] || c; }
function displayProducts(filterCategory = 'all') {
    const grid = document.getElementById('productsGrid');
    if (!grid) return;
    const filtered = filterCategory === 'all' ? products : products.filter(p => p.category === filterCategory);
    grid.innerHTML = filtered.map(product => `
        <div class="glass-card product-card">
            ${product.badge ? `<span class="product-badge">${product.badge}</span>` : ''}
            <span class="product-condition-badge">${getConditionText(product.condition)}</span>
            <div class="product-image-wrapper">
                <img src="${product.image}" alt="${product.name}" class="product-image" onerror="this.src='https://via.placeholder.com/400x350/1a1a1a/4CAF50?text='+encodeURIComponent(product.name)">
            </div>
            <div class="product-info">
                <h3 class="product-name">${product.name}</h3>
                <p class="product-description">${product.description.substring(0, 80)}...</p>
                <p class="product-location"><i class="fas fa-map-marker-alt"></i> ${product.location}</p>
                <div class="product-price">$${product.price.toFixed(2)}</div>
                <div class="product-actions">
                    <button class="glass-btn primary-btn" onclick="addToCart(${product.id})"><i class="fas fa-shopping-cart"></i> إضافة للسلة</button>
                    ${product.phone ? `<a href="tel:${product.phone}" class="glass-btn secondary-btn" title="اتصل بالبائع"><i class="fas fa-phone"></i></a>` : ''}
                </div>
            </div>
        </div>`).join('');
}
function filterProducts(category) {
    document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
    event.target.closest('.filter-btn').classList.add('active');
    displayProducts(category);
}
function addToCart(productId) {
    const product = products.find(p => p.id === productId);
    if (product) { cart.push({...product}); saveCart(); updateCartCount(); showToast('✅ تمت إضافة المنتج إلى السلة', 'success'); }
}
function updateCartCount() { const count = document.getElementById('cartCount'); if (count) count.textContent = cart.length; }
function toggleCart() { const modal = document.getElementById('cartModal'); modal.classList.toggle('active'); if (modal.classList.contains('active')) displayCartItems(); }
function displayCartItems() {
    const container = document.getElementById('cartItems');
    const total = document.getElementById('cartTotal');
    if (!container || !total) return;
    if (cart.length === 0) {
        container.innerHTML = '<div class="empty-cart-state"><i class="fas fa-shopping-bag"></i><p>سلة التسوق فارغة</p><span>ابدأ التسوق وأضف منتجاتك المفضلة</span></div>';
        total.textContent = '$0.00'; return;
    }
    container.innerHTML = cart.map((item, index) => `<div style="display:flex;gap:1rem;padding:1rem;margin-bottom:0.5rem;background:rgba(255,255,255,0.03);border-radius:15px;border:1px solid rgba(255,255,255,0.05);"><img src="${item.image}" style="width:60px;height:60px;object-fit:cover;border-radius:10px;" onerror="this.src='https://via.placeholder.com/60/1a1a1a/4CAF50'"><div style="flex:1;"><strong style="color:var(--gold);">${item.name}</strong><p style="color:var(--text-secondary);font-size:0.9rem;">$${item.price.toFixed(2)} | ${item.location}</p></div><button onclick="removeFromCart(${index})" style="background:none;border:none;color:#f44336;cursor:pointer;padding:0.5rem;"><i class="fas fa-trash"></i></button></div>`).join('');
    const sum = cart.reduce((s, item) => s + item.price, 0);
    total.textContent = `$${sum.toFixed(2)}`;
}
function removeFromCart(index) { cart.splice(index, 1); saveCart(); updateCartCount(); displayCartItems(); showToast('🗑️ تم حذف المنتج', 'error'); }
function checkout() {
    if (cart.length === 0) { showToast('⚠️ السلة فارغة', 'error'); return; }
    const total = cart.reduce((s, item) => s + item.price, 0);
    alert(`🛍️ شكراً لتسوقك مع كواغد!\\n💰 المجموع: $${total.toFixed(2)}\\n📦 عدد المنتجات: ${cart.length}\\n\\nسيتم التواصل مع البائعين لتنسيق التسليم`);
    cart = []; saveCart(); updateCartCount(); toggleCart(); showToast('🎉 تم إتمام الطلب بنجاح!', 'success');
}
document.addEventListener('DOMContentLoaded', () => {
    const sellForm = document.getElementById('sellForm');
    if (sellForm) {
        sellForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const newProduct = {
                id: Date.now(),
                name: document.getElementById('sellProductName').value,
                price: parseFloat(document.getElementById('sellProductPrice').value),
                category: document.getElementById('sellProductCategory').value,
                condition: document.getElementById('sellProductCondition').value,
                description: document.getElementById('sellProductDescription').value,
                location: document.getElementById('sellProductLocation').value,
                phone: document.getElementById('sellProductPhone').value,
                image: document.getElementById('sellProductImage').value || 'https://via.placeholder.com/400x350/1a1a1a/4CAF50?text=No+Image',
                badge: 'جديد'
            };
            products.unshift(newProduct);
            saveProducts(); displayProducts();
            sellForm.reset();
            document.getElementById('imagePreviewSell').innerHTML = '';
            showToast('🎉 تم إضافة منتجك بنجاح!', 'success');
            document.getElementById('products').scrollIntoView({ behavior: 'smooth' });
        });
    }
    displayProducts();
    updateCartCount();
});'''
    with open('js/products.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/products.js")

def create_admin_js():
    js = '''const ADMIN_PIN = '1234';
function showAdminLock() { document.getElementById('adminLockModal').classList.add('active'); document.getElementById('pin1').focus(); document.querySelectorAll('.pin-input').forEach(input => { input.value = ''; input.classList.remove('filled'); }); document.getElementById('pinError').textContent = ''; }
function closeAdminLock() { document.getElementById('adminLockModal').classList.remove('active'); }
function pinInput(input) { if (input.value) { input.classList.add('filled'); const next = input.nextElementSibling; if (next && next.classList.contains('pin-input')) next.focus(); } else { input.classList.remove('filled'); } }
function handlePinKey(event, input) { if (event.key === 'Backspace' && !input.value) { const prev = input.previousElementSibling; if (prev && prev.classList.contains('pin-input')) prev.focus(); } if (event.key === 'Enter') verifyPin(); }
function verifyPin() {
    const pin = Array.from(document.querySelectorAll('.pin-input')).map(input => input.value).join('');
    if (pin === ADMIN_PIN) { document.getElementById('adminLockModal').classList.remove('active'); document.getElementById('adminPanel').classList.add('active'); showToast('✅ تم الدخول إلى لوحة تحكم كواغد', 'success'); }
    else { document.getElementById('pinError').textContent = '❌ رمز الدخول غير صحيح'; document.querySelectorAll('.pin-input').forEach(input => { input.value = ''; input.classList.remove('filled'); }); document.getElementById('pin1').focus(); showToast('❌ رمز خاطئ!', 'error'); }
}
function closeAdminPanel() { document.getElementById('adminPanel').classList.remove('active'); showToast('👋 تم الخروج من لوحة التحكم', 'success'); }
async function handleImageUpload(event) {
    const file = event.target.files[0]; if (!file) return;
    const progress = document.getElementById('uploadProgress'); const preview = document.getElementById('imagePreview');
    progress.innerHTML = '<div style="color:var(--gold);"><i class="fas fa-spinner fa-spin"></i> جاري الرفع...</div>';
    const formData = new FormData(); formData.append('file', file); formData.append('upload_preset', 'kwaged-store'); formData.append('cloud_name', 'dmla61v7n');
    try {
        const response = await fetch('https://api.cloudinary.com/v1_1/dmla61v7n/image/upload', { method: 'POST', body: formData });
        const data = await response.json();
        document.getElementById('productImage').value = data.secure_url;
        preview.innerHTML = `<img src="${data.secure_url}" alt="Preview">`;
        progress.innerHTML = '<div style="color:#4CAF50;">✅ تم رفع الصورة بنجاح!</div>';
        showToast('✅ تم رفع الصورة بنجاح!', 'success');
    } catch (error) { progress.innerHTML = '<div style="color:#f44336;">❌ فشل رفع الصورة</div>'; showToast('❌ فشل رفع الصورة', 'error'); }
}
async function handleSellImageUpload(event) {
    const file = event.target.files[0]; if (!file) return;
    const progress = document.getElementById('uploadProgressSell'); const preview = document.getElementById('imagePreviewSell');
    progress.innerHTML = '<div style="color:var(--gold);"><i class="fas fa-spinner fa-spin"></i> جاري الرفع...</div>';
    const formData = new FormData(); formData.append('file', file); formData.append('upload_preset', 'kwaged-store'); formData.append('cloud_name', 'dmla61v7n');
    try {
        const response = await fetch('https://api.cloudinary.com/v1_1/dmla61v7n/image/upload', { method: 'POST', body: formData });
        const data = await response.json();
        document.getElementById('sellProductImage').value = data.secure_url;
        preview.innerHTML = `<img src="${data.secure_url}" alt="Preview">`;
        progress.innerHTML = '<div style="color:#4CAF50;">✅ تم رفع الصورة بنجاح!</div>';
        showToast('✅ تم رفع الصورة بنجاح!', 'success');
    } catch (error) { progress.innerHTML = '<div style="color:#f44336;">❌ فشل رفع الصورة</div>'; showToast('❌ فشل رفع الصورة', 'error'); }
}
document.getElementById('productForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const newProduct = { id: Date.now(), name: document.getElementById('productName').value, price: parseFloat(document.getElementById('productPrice').value), category: document.getElementById('productCategory').value, condition: document.getElementById('productCondition').value, description: document.getElementById('productDescription').value, image: document.getElementById('productImage').value, location: 'المتجر', phone: '', badge: 'إداري' };
    products.unshift(newProduct); saveProducts(); displayProducts(); resetAdminForm();
    showToast('🎉 تم إضافة المنتج بنجاح!', 'success');
});
function resetAdminForm() { document.getElementById('productForm').reset(); document.getElementById('imagePreview').innerHTML = ''; document.getElementById('uploadProgress').innerHTML = ''; }
function showToast(message, type = '') { const container = document.getElementById('toastContainer'); const toast = document.createElement('div'); toast.className = `toast ${type}`; toast.textContent = message; container.appendChild(toast); setTimeout(() => { toast.style.animation = 'slideInRight 0.3s ease reverse'; setTimeout(() => toast.remove(), 300); }, 3000); }'''
    with open('js/admin.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/admin.js")

def create_app_js():
    js = '''document.addEventListener('DOMContentLoaded', () => {
    window.addEventListener('scroll', () => { const nav = document.querySelector('.glass-nav'); if (window.scrollY > 100) nav.classList.add('scrolled'); else nav.classList.remove('scrolled'); });
    document.querySelectorAll('a[href^="#"]').forEach(anchor => { anchor.addEventListener('click', function(e) { e.preventDefault(); const target = document.querySelector(this.getAttribute('href')); if (target) target.scrollIntoView({ behavior: 'smooth' }); }); });
    window.addEventListener('click', (e) => { if (e.target.classList.contains('glass-modal')) e.target.classList.remove('active'); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') document.querySelectorAll('.modal.active').forEach(m => m.classList.remove('active')); });
    const contactForm = document.getElementById('contactForm'); if (contactForm) { contactForm.addEventListener('submit', (e) => { e.preventDefault(); showToast('✅ تم إرسال رسالتك بنجاح!', 'success'); contactForm.reset(); }); }
    setupDragDrop('uploadArea', 'imageUpload'); setupDragDrop('uploadAreaSell', 'imageUploadSell');
});
function setupDragDrop(areaId, inputId) { const uploadArea = document.getElementById(areaId); if (!uploadArea) return; ['dragenter','dragover','dragleave','drop'].forEach(eventName => { uploadArea.addEventListener(eventName, preventDefaults); }); ['dragenter','dragover'].forEach(eventName => { uploadArea.addEventListener(eventName, () => uploadArea.classList.add('highlight')); }); ['dragleave','drop'].forEach(eventName => { uploadArea.addEventListener(eventName, () => uploadArea.classList.remove('highlight')); }); uploadArea.addEventListener('drop', (e) => { const file = e.dataTransfer.files[0]; if (file && file.type.startsWith('image/')) { const input = document.getElementById(inputId); const dt = new DataTransfer(); dt.items.add(file); input.files = dt.files; input.dispatchEvent(new Event('change')); } }); }
function preventDefaults(e) { e.preventDefault(); e.stopPropagation(); }
function scrollToSection(id) { const element = document.getElementById(id); if (element) element.scrollIntoView({ behavior: 'smooth' }); }'''
    with open('js/app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("✅ تم إنشاء: js/app.js")

def main():
    print("🌟 بدء إنشاء سوق كواغد للأغراض المستعملة...")
    create_directory_structure()
    create_index_html()
    create_glass_morphism_css()
    create_bubbles_css()
    create_style_css()
    create_admin_css()
    create_products_js()
    create_admin_js()
    create_app_js()
    print("🎉 تم إنشاء جميع ملفات سوق كواغد بنجاح!")
    print("🏪 الاسم: كواغد | 💵 العملة: دولار | 🔐 الرمز: 1234")

if __name__ == "__main__":
    main()
