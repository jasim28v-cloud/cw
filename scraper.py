#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                    متجر كواغد - KAWAGHED Store                ║
║              الجيل الجديد من المتاجر الرقمية العربية           ║
║                   powered by Cloudinary AI                    ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import time
import random
import shutil
import hashlib
import base64
import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from enum import Enum
import secrets

# تثبيت المكتبات المطلوبة تلقائياً
required_packages = ['Pillow', 'requests']
for package in required_packages:
    try:
        __import__(package.lower())
    except ImportError:
        os.system(f'{sys.executable} -m pip install {package} --quiet')

try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
    import requests
except ImportError:
    pass

# ═══════════════════════════════════════════════════════════════
# الإعدادات المتقدمة
# ═══════════════════════════════════════════════════════════════

class StoreTheme(Enum):
    DARK_NEON = "dark-neon"
    GLASS_MORPHISM = "glass-morphism" 
    MINIMAL_GOLD = "minimal-gold"
    CYBER_PUNK = "cyber-punk"

@dataclass
class StoreConfig:
    """إعدادات المتجر المتقدمة"""
    name: str = "كواغد"
    slogan: str = "حيث تلتقي الجودة بالأناقة ✨"
    version: str = "3.0.0"
    theme: StoreTheme = StoreTheme.GLASS_MORPHISM
    cloud_name: str = "dk9xej3cf"
    upload_preset: str = "k30_mk"
    security_code: str = "1234"
    currency: str = "USD"
    language: str = "ar"
    direction: str = "rtl"
    primary_color: str = "#6C5CE7"
    secondary_color: str = "#A8E6CF"
    accent_color: str = "#FFD93D"
    enable_ai_suggestions: bool = True
    enable_3d_effects: bool = True
    enable_parallax: bool = True
    enable_dark_mode: bool = True
    enable_pwa: bool = True
    enable_push_notifications: bool = True
    max_upload_size: int = 20  # MB
    allowed_formats: List[str] = None
    
    def __post_init__(self):
        if self.allowed_formats is None:
            self.allowed_formats = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'avif', 'svg']

# ═══════════════════════════════════════════════════════════════
# نظام التشفير والأمان المتقدم
# ═══════════════════════════════════════════════════════════════

class SecuritySystem:
    """نظام الأمان المتقدم للمتجر"""
    
    @staticmethod
    def generate_token(length: int = 64) -> str:
        """توليد رمز أمان عشوائي"""
        return secrets.token_hex(length // 2)
    
    @staticmethod
    def hash_password(password: str, salt: str = None) -> Tuple[str, str]:
        """تشفير كلمة المرور مع salt"""
        if salt is None:
            salt = secrets.token_hex(16)
        hash_obj = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt.encode('utf-8'),
            100000
        )
        return hash_obj.hex(), salt
    
    @staticmethod
    def verify_password(password: str, hash_value: str, salt: str) -> bool:
        """التحقق من كلمة المرور"""
        new_hash, _ = SecuritySystem.hash_password(password, salt)
        return new_hash == hash_value
    
    @staticmethod
    def obfuscate_code(code: str) -> str:
        """تشويش الرمز الأمني"""
        # تحويل الرمز إلى base64 مع إضافة تشويش
        encoded = base64.b64encode(code.encode()).decode()
        shuffled = ''.join(random.sample(encoded, len(encoded)))
        return base64.b64encode(shuffled.encode()).decode()

# ═══════════════════════════════════════════════════════════════
# مولد CSS المتقدم
# ═══════════════════════════════════════════════════════════════

class CSSGenerator:
    """مولد أكواد CSS احترافية"""
    
    @staticmethod
    def generate_advanced_css(config: StoreConfig) -> str:
        """توليد CSS متقدم مع تأثيرات عصرية"""
        
        css_code = f'''/* ╔══════════════════════════════════════════════════════╗
   ║     متجر كواغد - KAWAGHED Store v{config.version}        ║
   ║   تصميم احترافي بمواصفات 2024 - Arab eCommerce        ║
   ╚══════════════════════════════════════════════════════╝ */

@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900;1000&family=El+Messiri:wght@400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

:root {{
    /* لوحة الألوان المتقدمة */
    --primary: {config.primary_color};
    --primary-light: {config._lighten_color(config.primary_color)};
    --primary-dark: {config._darken_color(config.primary_color)};
    --secondary: {config.secondary_color};
    --accent: {config.accent_color};
    
    /* ألوان الوضع الليلي */
    --bg-primary: #0a0a1a;
    --bg-secondary: #1a1a2e;
    --bg-tertiary: #16213e;
    
    /* تأثيرات زجاجية */
    --glass-bg: rgba(255, 255, 255, 0.03);
    --glass-border: rgba(255, 255, 255, 0.1);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    --glass-blur: blur(20px);
    
    /* تأثيرات النيون */
    --neon-primary: 0 0 10px {config.primary_color},
                     0 0 20px {config.primary_color},
                     0 0 40px {config.primary_color};
    --neon-accent: 0 0 10px {config.accent_color},
                   0 0 20px {config.accent_color};
    
    /* القياسات */
    --radius-sm: 10px;
    --radius-md: 20px;
    --radius-lg: 30px;
    --radius-xl: 50px;
    --radius-full: 50%;
    
    /* الحركات */
    --transition-fast: 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-smooth: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-bounce: 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    
    /* الطبقات */
    --z-base: 1;
    --z-dropdown: 100;
    --z-sticky: 200;
    --z-overlay: 300;
    --z-modal: 400;
    --z-toast: 500;
}}

* {{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
    font-size: 16px;
}}

body {{
    font-family: 'Cairo', 'El Messiri', sans-serif;
    background: var(--bg-primary);
    color: #ffffff;
    line-height: 1.6;
    overflow-x: hidden;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}}

/* ═══════════════════════════════════════════════════════
   تأثيرات الخلفية المتقدمة
   ═══════════════════════════════════════════════════════ */

.background-effects {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
}}

.gradient-orb {{
    position: absolute;
    border-radius: 50%;
    filter: blur(80px);
    opacity: 0.3;
    animation: floatOrb 20s infinite ease-in-out;
}}

.gradient-orb:nth-child(1) {{
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, {config.primary_color}44, transparent 70%);
    top: -100px;
    left: -100px;
    animation-delay: 0s;
}}

.gradient-orb:nth-child(2) {{
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, {config.secondary_color}44, transparent 70%);
    bottom: -100px;
    right: -100px;
    animation-delay: -7s;
}}

.gradient-orb:nth-child(3) {{
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, {config.accent_color}44, transparent 70%);
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    animation-delay: -14s;
}}

@keyframes floatOrb {{
    0%, 100% {{ transform: translate(0, 0) scale(1); }}
    25% {{ transform: translate(100px, -50px) scale(1.1); }}
    50% {{ transform: translate(50px, 100px) scale(0.9); }}
    75% {{ transform: translate(-100px, 50px) scale(1.05); }}
}}

/* ═══════════════════════════════════════════════════════
   الحاوية الزجاجية المتقدمة
   ═══════════════════════════════════════════════════════ */

.glass-container {{
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    box-shadow: var(--glass-shadow);
    transition: all var(--transition-smooth);
}}

.glass-container:hover {{
    border-color: {config.primary_color}44;
    box-shadow: var(--glass-shadow), var(--neon-primary);
}}

/* ═══════════════════════════════════════════════════════
   الهيدر المتطور
   ═══════════════════════════════════════════════════════ */

.kawaghed-header {{
    position: sticky;
    top: 20px;
    z-index: var(--z-sticky);
    padding: 25px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    animation: slideDownFade 0.8s cubic-bezier(0.4, 0, 0.2, 1);
    margin: 20px;
}}

@keyframes slideDownFade {{
    from {{
        transform: translateY(-30px);
        opacity: 0;
        filter: blur(10px);
    }}
    to {{
        transform: translateY(0);
        opacity: 1;
        filter: blur(0);
    }}
}}

.logo-wrapper {{
    display: flex;
    align-items: center;
    gap: 15px;
}}

.logo-animation {{
    position: relative;
    width: 60px;
    height: 60px;
}}

.logo-circle {{
    position: absolute;
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, {config.primary_color}, {config.secondary_color});
    animation: rotateLogo 3s linear infinite;
}}

.logo-circle::before {{
    content: '';
    position: absolute;
    inset: 3px;
    background: var(--bg-primary);
    border-radius: 50%;
}}

.logo-inner {{
    position: absolute;
    inset: 6px;
    border-radius: 50%;
    background: linear-gradient(135deg, {config.primary_color}44, {config.secondary_color}44);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 900;
}}

@keyframes rotateLogo {{
    from {{ transform: rotate(0deg); }}
    to {{ transform: rotate(360deg); }}
}}

.logo-text-wrapper {{
    display: flex;
    flex-direction: column;
}}

.logo-main-text {{
    font-size: 32px;
    font-weight: 900;
    background: linear-gradient(135deg, {config.primary_color}, {config.accent_color});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -1px;
}}

.logo-sub-text {{
    font-size: 12px;
    color: {config.accent_color};
    opacity: 0.8;
    letter-spacing: 2px;
    text-transform: uppercase;
}}

/* ═══════════════════════════════════════════════════════
   الأزرار المتطورة
   ═══════════════════════════════════════════════════════ */

.btn-kawaghed {{
    position: relative;
    padding: 15px 35px;
    border: none;
    border-radius: var(--radius-xl);
    font-family: 'Cairo', sans-serif;
    font-size: 16px;
    font-weight: 700;
    cursor: pointer;
    overflow: hidden;
    transition: all var(--transition-bounce);
    text-transform: uppercase;
    letter-spacing: 1px;
    color: white;
    background: linear-gradient(135deg, {config.primary_color}, {config._darken_color(config.primary_color)});
    box-shadow: 0 10px 30px {config.primary_color}44;
}}

.btn-kawaghed::before {{
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: left 0.5s;
}}

.btn-kawaghed:hover {{
    transform: translateY(-3px);
    box-shadow: 0 15px 40px {config.primary_color}66, var(--neon-primary);
}}

.btn-kawaghed:hover::before {{
    left: 100%;
}}

.btn-kawaghed:active {{
    transform: translateY(-1px);
}}

/* ═══════════════════════════════════════════════════════
   شبكة المنتجات المتطورة
   ═══════════════════════════════════════════════════════ */

.products-grid-kawaghed {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 30px;
    padding: 40px 20px;
    perspective: 1000px;
}}

.product-card-kawaghed {{
    position: relative;
    background: var(--glass-bg);
    backdrop-filter: var(--glass-blur);
    -webkit-backdrop-filter: var(--glass-blur);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    transition: all var(--transition-smooth);
    animation: cardAppear 0.6s cubic-bezier(0.4, 0, 0.2, 1) backwards;
    transform-style: preserve-3d;
}}

.product-card-kawaghed:hover {{
    transform: translateY(-10px) rotateX(5deg);
    border-color: {config.primary_color}66;
    box-shadow: 0 30px 60px rgba(0,0,0,0.3), var(--neon-primary);
}}

@keyframes cardAppear {{
    from {{
        opacity: 0;
        transform: translateY(50px) rotateX(-10deg);
    }}
    to {{
        opacity: 1;
        transform: translateY(0) rotateX(0);
    }}
}}

.product-image-wrapper {{
    position: relative;
    height: 280px;
    overflow: hidden;
}}

.product-image {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}}

.product-card-kawaghed:hover .product-image {{
    transform: scale(1.08);
}}

.product-overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.8) 0%, transparent 50%);
    opacity: 0;
    transition: opacity var(--transition-smooth);
    display: flex;
    align-items: flex-end;
    justify-content: center;
    padding: 20px;
}}

.product-card-kawaghed:hover .product-overlay {{
    opacity: 1;
}}

.product-badge-kawaghed {{
    position: absolute;
    top: 15px;
    right: 15px;
    background: linear-gradient(135deg, {config.accent_color}, #FFA500);
    color: #000;
    padding: 8px 16px;
    border-radius: var(--radius-xl);
    font-weight: 700;
    font-size: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
    animation: badgePulse 2s infinite;
}}

@keyframes badgePulse {{
    0%, 100% {{ box-shadow: 0 5px 15px rgba(0,0,0,0.3); }}
    50% {{ box-shadow: 0 5px 25px {config.accent_color}88; }}
}}

.product-info-kawaghed {{
    padding: 25px;
}}

.product-name-kawaghed {{
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #fff;
}}

.product-price-kawaghed {{
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(135deg, {config.primary_color}, {config.accent_color});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}}

.product-price-kawaghed::before {{
    content: '$';
    font-size: 20px;
}}

/* ═══════════════════════════════════════════════════════
   المودال المتطور
   ═══════════════════════════════════════════════════════ */

.modal-kawaghed {{
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(10px);
    z-index: var(--z-modal);
    align-items: center;
    justify-content: center;
    animation: modalFadeIn 0.3s ease;
}}

.modal-kawaghed.active {{
    display: flex;
}}

@keyframes modalFadeIn {{
    from {{ opacity: 0; }}
    to {{ opacity: 1; }}
}}

.modal-content-kawaghed {{
    background: var(--bg-secondary);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    padding: 40px;
    max-width: 500px;
    width: 90%;
    box-shadow: 0 40px 80px rgba(0,0,0,0.5);
    animation: modalSlideUp 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}}

@keyframes modalSlideUp {{
    from {{
        transform: translateY(50px) scale(0.95);
        opacity: 0;
    }}
    to {{
        transform: translateY(0) scale(1);
        opacity: 1;
    }}
}}

/* ═══════════════════════════════════════════════════════
   التأثيرات الخاصة
   ═══════════════════════════════════════════════════════ */

.typing-effect::after {{
    content: '|';
    animation: typing 1s infinite;
}}

@keyframes typing {{
    0%, 100% {{ opacity: 1; }}
    50% {{ opacity: 0; }}
}}

/* تأثيرات الجسيمات */
.particles {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: -1;
}}

.particle {{
    position: absolute;
    width: 3px;
    height: 3px;
    background: {config.primary_color};
    border-radius: 50%;
    animation: particleFloat 10s infinite;
}}

@keyframes particleFloat {{
    0%, 100% {{
        transform: translateY(100vh) translateX(0);
        opacity: 0;
    }}
    10% {{
        opacity: 1;
    }}
    90% {{
        opacity: 1;
    }}
    100% {{
        transform: translateY(-100vh) translateX(100px);
        opacity: 0;
    }}
}}

/* الريسبونسف المتقدم */
@media (max-width: 768px) {{
    .kawaghed-header {{
        flex-direction: column;
        gap: 20px;
        padding: 20px;
        margin: 10px;
    }}
    
    .products-grid-kawaghed {{
        grid-template-columns: 1fr;
        padding: 20px 10px;
    }}
    
    .logo-main-text {{
        font-size: 24px;
    }}
}}

/* دعم المتصفحات القديمة */
@supports not (backdrop-filter: blur(20px)) {{
    .glass-container,
    .product-card-kawaghed {{
        background: rgba(26, 26, 46, 0.9);
    }}
}}
'''
        return css_code

# ═══════════════════════════════════════════════════════════════
# مولد JavaScript المتقدم
# ═══════════════════════════════════════════════════════════════

class JSGenerator:
    """مولد أكواد JavaScript احترافية"""
    
    @staticmethod
    def generate_advanced_js(config: StoreConfig) -> str:
        """توليد JavaScript متقدم مع ميزات عصرية"""
        
        js_code = f'''/* ╔══════════════════════════════════════════════════════╗
   ║     متجر كواغد - JavaScript Engine v{config.version}     ║
   ╚══════════════════════════════════════════════════════╝ */

'use strict';

class KawaghedStore {{
    constructor() {{
        this.config = {json.dumps(asdict(config), ensure_ascii=False)};
        this.cloudName = '{config.cloud_name}';
        this.uploadPreset = '{config.upload_preset}';
        this.securityCode = '{config.security_code}';
        this.products = [];
        this.isOnline = navigator.onLine;
        this.init();
    }}
    
    async init() {{
        console.log('🔥 متجر كواغد يشتعل!');
        this.createParticles();
        this.createBackgroundEffects();
        this.loadProducts();
        this.attachEvents();
        this.displayProducts();
        this.checkConnection();
        await this.registerServiceWorker();
    }}
    
    createParticles() {{
        const particlesContainer = document.createElement('div');
        particlesContainer.className = 'particles';
        
        for (let i = 0; i < 50; i++) {{
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 10 + 's';
            particle.style.animationDuration = (Math.random() * 10 + 10) + 's';
            particlesContainer.appendChild(particle);
        }}
        
        document.body.appendChild(particlesContainer);
    }}
    
    createBackgroundEffects() {{
        const effectsContainer = document.createElement('div');
        effectsContainer.className = 'background-effects';
        
        for (let i = 0; i < 3; i++) {{
            const orb = document.createElement('div');
            orb.className = 'gradient-orb';
            effectsContainer.appendChild(orb);
        }}
        
        document.body.insertBefore(effectsContainer, document.body.firstChild);
    }}
    
    async openCloudinaryWidget() {{
        const password = await this.showSecurityPrompt();
        
        if (password !== this.securityCode) {{
            await this.showToast('❌ رمز التفعيل غير صحيح!', 'error');
            return;
        }}
        
        if (!window.cloudinary) {{
            await this.loadCloudinaryScript();
        }}
        
        this.createUploadWidget();
    }}
    
    showSecurityPrompt() {{
        return new Promise((resolve) => {{
            const overlay = document.createElement('div');
            overlay.style.cssText = `
                position: fixed;
                inset: 0;
                background: rgba(0,0,0,0.9);
                z-index: 10000;
                display: flex;
                align-items: center;
                justify-content: center;
                backdrop-filter: blur(10px);
            `;
            
            const dialog = document.createElement('div');
            dialog.style.cssText = `
                background: var(--bg-secondary);
                padding: 40px;
                border-radius: 30px;
                text-align: center;
                border: 1px solid var(--glass-border);
                animation: modalSlideUp 0.3s ease;
                max-width: 400px;
                width: 90%;
            `;
            
            dialog.innerHTML = `
                <div style="font-size: 60px; margin-bottom: 20px;">🔐</div>
                <h2 style="margin-bottom: 20px; font-size: 24px; color: white;">التحقق الأمني</h2>
                <p style="color: #999; margin-bottom: 20px;">أدخل رمز التفعيل للمتابعة</p>
                <div style="position: relative;">
                    <input type="password" 
                           id="securityInput" 
                           placeholder="••••" 
                           maxlength="4"
                           style="width: 100%;
                                  padding: 20px;
                                  font-size: 32px;
                                  text-align: center;
                                  background: rgba(255,255,255,0.05);
                                  border: 2px solid rgba(255,255,255,0.1);
                                  border-radius: 20px;
                                  color: white;
                                  letter-spacing: 10px;
                                  font-family: 'Cairo', sans-serif;
                                  outline: none;
                                  transition: all 0.3s ease;">
                </div>
                <div class="button-group" style="display: flex; gap: 10px; margin-top: 20px;">
                    <button id="confirmBtn" 
                            style="flex: 1;
                                   padding: 15px;
                                   background: linear-gradient(135deg, {config.primary_color}, {config._darken_color(config.primary_color)});
                                   border: none;
                                   border-radius: 50px;
                                   color: white;
                                   font-weight: 700;
                                   cursor: pointer;
                                   font-family: 'Cairo', sans-serif;">
                        تأكيد
                    </button>
                    <button id="cancelBtn"
                            style="flex: 1;
                                   padding: 15px;
                                   background: rgba(255,255,255,0.1);
                                   border: none;
                                   border-radius: 50px;
                                   color: white;
                                   font-weight: 700;
                                   cursor: pointer;
                                   font-family: 'Cairo', sans-serif;">
                        إلغاء
                    </button>
                </div>
            `;
            
            overlay.appendChild(dialog);
            document.body.appendChild(overlay);
            
            const input = document.getElementById('securityInput');
            const confirmBtn = document.getElementById('confirmBtn');
            const cancelBtn = document.getElementById('cancelBtn');
            
            input.focus();
            
            const handleConfirm = () => {{
                const value = input.value;
                document.body.removeChild(overlay);
                resolve(value);
            }};
            
            const handleCancel = () => {{
                document.body.removeChild(overlay);
                resolve(null);
            }};
            
            confirmBtn.addEventListener('click', handleConfirm);
            cancelBtn.addEventListener('click', handleCancel);
            
            input.addEventListener('keypress', (e) => {{
                if (e.key === 'Enter') {{
                    handleConfirm();
                }}
            }});
        }});
    }}
    
    createUploadWidget() {{
        const widget = window.cloudinary.createUploadWidget({{
            cloudName: this.cloudName,
            uploadPreset: this.uploadPreset,
            maxFiles: 1,
            resourceType: 'image',
            clientAllowedFormats: this.config.allowed_formats,
            maxFileSize: this.config.max_upload_size * 1000000,
            language: 'ar',
            styles: {{
                palette: {{
                    window: '#1a1a2e',
                    windowBorder: '{config.primary_color}',
                    tabIcon: '{config.primary_color}',
                    menuIcons: '{config.secondary_color}',
                    textDark: '#ffffff',
                    textLight: '#1a1a2e',
                    link: '{config.primary_color}',
                    action: '{config.primary_color}',
                    inactiveTabIcon: '#666',
                    error: '#f44336',
                    inProgress: '{config.primary_color}',
                    complete: '#4CAF50',
                    sourceBg: '#0a0a1a'
                }}
            }}
        }}, (error, result) => {{
            if (error) {{
                this.showToast('❌ حدث خطأ في رفع الصورة', 'error');
                return;
            }}
            
            if (result?.event === 'success') {{
                this.handleImageUpload(result.info);
            }}
        }});
        
        widget.open();
    }}
    
    handleImageUpload(imageInfo) {{
        document.getElementById('imageUrl').value = imageInfo.secure_url;
        
        const preview = `
            <div style="text-align: center;">
                <div style="font-size: 48px;">✅</div>
                <p>تم رفع الصورة بنجاح!</p>
                <img src="${{imageInfo.secure_url}}" 
                     style="width: 120px; 
                            height: 120px; 
                            object-fit: cover; 
                            border-radius: 20px; 
                            border: 3px solid {config.primary_color};
                            box-shadow: 0 10px 30px {config.primary_color}44;
                            margin-top: 15px;">
                <p style="margin-top: 10px; color: #999; font-size: 12px;">
                    ${{(imageInfo.bytes / 1024).toFixed(1)}} KB
                </p>
            </div>
        `;
        
        document.getElementById('uploadStatus').innerHTML = preview;
        this.showToast('✅ تم رفع الصورة بنجاح!', 'success');
    }}
    
    addProduct(event) {{
        event.preventDefault();
        
        const imageUrl = document.getElementById('imageUrl').value;
        const name = document.getElementById('productName').value;
        const price = document.getElementById('productPrice').value;
        
        if (!imageUrl) {{
            this.showToast('⚠️ الرجاء رفع صورة للمنتج', 'warning');
            return;
        }}
        
        const product = {{
            id: Date.now().toString(36) + Math.random().toString(36).substr(2),
            name,
            price: parseFloat(price),
            image: imageUrl,
            date: new Date().toLocaleDateString('ar-SA', {{ 
                year: 'numeric', 
                month: 'long', 
                day: 'numeric' 
            }}),
            timestamp: new Date().toISOString()
        }};
        
        this.products.unshift(product);
        this.saveProducts();
        this.displayProducts();
        this.closeModal();
        
        this.showToast('🎉 تم نشر المنتج بنجاح!', 'success');
    }}
    
    deleteProduct(id) {{
        const confirmDialog = document.createElement('div');
        confirmDialog.style.cssText = `
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.9);
            z-index: 10000;
            display: flex;
            align-items: center;
            justify-content: center;
            backdrop-filter: blur(10px);
        `;
        
        confirmDialog.innerHTML = `
            <div style="background: var(--bg-secondary); 
                        padding: 40px; 
                        border-radius: 30px; 
                        text-align: center;
                        border: 1px solid var(--glass-border);
                        max-width: 400px;
                        width: 90%;
                        animation: modalSlideUp 0.3s ease;">
                <div style="font-size: 60px;">🗑️</div>
                <h2 style="color: white; margin: 20px 0;">تأكيد الحذف</h2>
                <p style="color: #999; margin-bottom: 20px;">هل أنت متأكد من حذف هذا المنتج؟</p>
                <div style="display: flex; gap: 10px;">
                    <button id="confirmDelete" 
                            style="flex: 1; 
                                   padding: 15px; 
                                   background: #f44336; 
                                   border: none; 
                                   border-radius: 50px; 
                                   color: white; 
                                   font-weight: 700; 
                                   cursor: pointer;
                                   font-family: 'Cairo', sans-serif;">
                        حذف
                    </button>
                    <button id="cancelDelete"
                            style="flex: 1; 
                                   padding: 15px; 
                                   background: rgba(255,255,255,0.1); 
                                   border: none; 
                                   border-radius: 50px; 
                                   color: white; 
                                   font-weight: 700; 
                                   cursor: pointer;
                                   font-family: 'Cairo', sans-serif;">
                        إلغاء
                    </button>
                </div>
            </div>
        `;
        
        document.body.appendChild(confirmDialog);
        
        document.getElementById('confirmDelete').onclick = () => {{
            this.products = this.products.filter(p => p.id !== id);
            this.saveProducts();
            this.displayProducts();
            document.body.removeChild(confirmDialog);
            this.showToast('✅ تم حذف المنتج', 'success');
        }};
        
        document.getElementById('cancelDelete').onclick = () => {{
            document.body.removeChild(confirmDialog);
        }};
    }}
    
    showToast(message, type = 'info') {{
        const toast = document.createElement('div');
        const colors = {{
            success: '#4CAF50',
            error: '#f44336',
            warning: '#ff9800',
            info: '{config.primary_color}'
        }};
        
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            padding: 15px 30px;
            background: ${{colors[type] || colors.info}};
            color: white;
            border-radius: 50px;
            font-weight: 700;
            z-index: 10001;
            animation: slideDownFade 0.3s ease;
            box-shadow: 0 10px 30px ${{colors[type]}}44;
            font-family: 'Cairo', sans-serif;
            max-width: 90%;
            text-align: center;
        `;
        
        toast.textContent = message;
        document.body.appendChild(toast);
        
        setTimeout(() => {{
            toast.style.animation = 'slideUpFade 0.3s ease';
            setTimeout(() => document.body.removeChild(toast), 300);
        }}, 4000);
    }}
    
    async checkConnection() {{
        window.addEventListener('online', () => {{
            this.isOnline = true;
            this.showToast('✅ تم استعادة الاتصال بالإنترنت', 'success');
        }});
        
        window.addEventListener('offline', () => {{
            this.isOnline = false;
            this.showToast('⚠️ أنت غير متصل بالإنترنت', 'warning');
        }});
    }}
    
    async registerServiceWorker() {{
        if ('serviceWorker' in navigator) {{
            try {{
                const registration = await navigator.serviceWorker.register('/sw.js');
                console.log('✅ Service Worker registered:', registration);
            }} catch (error) {{
                console.log('Service Worker registration failed:', error);
            }}
        }}
    }}
    
    saveProducts() {{
        localStorage.setItem('kawaghed_products', JSON.stringify(this.products));
        
        const backup = {{
            products: this.products,
            timestamp: new Date().toISOString(),
            version: '{config.version}'
        }};
        localStorage.setItem('kawaghed_backup', JSON.stringify(backup));
    }}
    
    loadProducts() {{
        const saved = localStorage.getItem('kawaghed_products');
        if (saved) {{
            this.products = JSON.parse(saved);
        }} else {{
            this.products = this.getDemoProducts();
            this.saveProducts();
        }}
    }}
    
    getDemoProducts() {{
        return [
            {{
                id: 'k1',
                name: 'ساعة كواغد الذكية',
                price: 499.99,
                image: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600',
                date: new Date().toLocaleDateString('ar-SA'),
                timestamp: new Date().toISOString()
            }},
            {{
                id: 'k2',
                name: 'سماعات كواغد برو',
                price: 299.99,
                image: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600',
                date: new Date().toLocaleDateString('ar-SA'),
                timestamp: new Date().toISOString()
            }}
        ];
    }}
    
    displayProducts() {{
        const grid = document.getElementById('productsGrid');
        
        if (!this.products.length) {{
            grid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 80px 20px;">
                    <div style="font-size: 100px; animation: floatOrb 3s infinite;">🛍️</div>
                    <h2 style="color: white; margin: 20px 0;">متجر كواغد الفاخر</h2>
                    <p style="color: #999; font-size: 18px;">أضف منتجك الأول وابدأ رحلة البيع</p>
                </div>
            `;
            return;
        }}
        
        grid.innerHTML = this.products.map((product, index) => `
            <div class="product-card-kawaghed" style="animation-delay: ${{index * 0.1}}s">
                <div class="product-image-wrapper">
                    <img src="${{product.image}}" 
                         alt="${{product.name}}" 
                         class="product-image"
                         loading="lazy"
                         onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 400 300%22><rect fill=%22%231a1a2e%22 width=%22400%22 height=%22300%22/><text fill=%22%23666%22 x=%2250%25%22 y=%2250%25%22 text-anchor=%22middle%22 dy=%22.3em%22 font-size=%2220%22>📷 صورة المنتج</text></svg>'">
                    <div class="product-badge-kawaghed">كواغد</div>
                    <div class="product-overlay">
                        <button class="btn-kawaghed" onclick="kawaghedStore.deleteProduct('${{product.id}}')">
                            🗑️ حذف
                        </button>
                    </div>
                </div>
                <div class="product-info-kawaghed">
                    <h3 class="product-name-kawaghed">${{product.name}}</h3>
                    <div class="product-price-kawaghed">${{product.price.toFixed(2)}}</div>
                    <p style="color: #999; font-size: 12px; margin-top: 10px;">
                        📅 ${{product.date}}
                    </p>
                </div>
            </div>
        `).join('');
    }}
    
    attachEvents() {{
        document.getElementById('productModal').addEventListener('click', (e) => {{
            if (e.target === e.currentTarget) this.closeModal();
        }});
        
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') this.closeModal();
        }});
        
        document.getElementById('productForm').addEventListener('submit', (e) => {{
            this.addProduct(e);
        }});
    }}
    
    openModal() {{
        document.getElementById('productModal').classList.add('active');
        document.getElementById('uploadStatus').innerHTML = '⏳ جاري انتظار رفع الصورة...';
        document.getElementById('productForm').reset();
    }}
    
    closeModal() {{
        document.getElementById('productModal').classList.remove('active');
    }}
}}

// بدء تشغيل المتجر
const kawaghedStore = new KawaghedStore();
window.kawaghedStore = kawaghedStore;

// دوال عامة
function openCloudinaryWidget() {{ kawaghedStore.openCloudinaryWidget(); }}
function closeModal() {{ kawaghedStore.closeModal(); }}
function openAddProductModal() {{ kawaghedStore.openModal(); }}
'''
        return js_code

# ═══════════════════════════════════════════════════════════════
# نظام التوليد الرئيسي
# ═══════════════════════════════════════════════════════════════

class KawaghedStoreGenerator:
    """المولد الرئيسي لمتجر كواغد"""
    
    def __init__(self):
        self.config = StoreConfig()
        self.css_gen = CSSGenerator()
        self.js_gen = JSGenerator()
        self.files_created = []
        
    def create_directory_structure(self):
        """إنشاء هيكل المشروع"""
        dirs = [
            'assets/css',
            'assets/js',
            'assets/images',
            'assets/fonts',
            'data',
            'backups',
            '.github/workflows',
            'sw'  # Service Workers
        ]
        
        for d in dirs:
            Path(d).mkdir(parents=True, exist_ok=True)
            
    def generate_html(self) -> str:
        """توليد HTML خارق"""
        return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="theme-color" content="{self.config.primary_color}">
    <meta name="description" content="{self.config.slogan}">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    
    <title>متجر كواغد | Kawaghed Store</title>
    
    <link rel="stylesheet" href="assets/css/style.css">
    <link rel="manifest" href="manifest.json">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔥</text></svg>">
    
    <script src="https://upload-widget.cloudinary.com/global/all.js" defer></script>
</head>
<body>
    <div class="container">
        <header class="kawaghed-header glass-container">
            <div class="logo-wrapper">
                <div class="logo-animation">
                    <div class="logo-circle"></div>
                    <div class="logo-inner">🔥</div>
                </div>
                <div class="logo-text-wrapper">
                    <span class="logo-main-text">كواغد</span>
                    <span class="logo-sub-text">Kawaghed Store</span>
                </div>
            </div>
            <div style="display: flex; gap: 15px;">
                <button class="btn-kawaghed" onclick="openAddProductModal()">
                    ✨ إضافة منتج
                </button>
            </div>
        </header>
        
        <main>
            <div class="products-grid-kawaghed" id="productsGrid"></div>
        </main>
    </div>
    
    <div class="modal-kawaghed" id="productModal">
        <div class="modal-content-kawaghed">
            <h2 style="text-align: center; margin-bottom: 30px; font-size: 28px; font-weight: 900;
                       background: linear-gradient(135deg, {self.config.primary_color}, {self.config.accent_color});
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                🚀 أضف منتجك إلى كواغد
            </h2>
            
            <div id="uploadStatus" style="text-align: center; padding: 20px; 
                                            background: rgba(255,255,255,0.03); 
                                            border-radius: 20px; 
                                            margin-bottom: 20px; 
                                            border: 2px dashed rgba(255,255,255,0.1);">
                ☁️ اسحب وأفلت الصورة هنا أو اضغط للرفع
            </div>
            
            <form id="productForm">
                <div class="form-group" style="margin-bottom: 20px;">
                    <button type="button" class="btn-kawaghed" 
                            onclick="openCloudinaryWidget()" 
                            style="width: 100%; background: #4CAF50;">
                        ☁️ رفع إلى السحابة
                    </button>
                    <input type="hidden" id="imageUrl" required>
                </div>
                
                <div class="form-group" style="margin-bottom: 20px;">
                    <label style="display: block; color: #999; margin-bottom: 10px;">📝 اسم المنتج</label>
                    <input type="text" id="productName" required 
                           style="width: 100%; padding: 15px; background: rgba(255,255,255,0.05);
                                  border: 2px solid rgba(255,255,255,0.1); border-radius: 15px;
                                  color: white; font-family: 'Cairo'; font-size: 16px;"
                           placeholder="مثلاً: ساعة كواغد الذكية">
                </div>
                
                <div class="form-group" style="margin-bottom: 20px;">
                    <label style="display: block; color: #999; margin-bottom: 10px;">💰 السعر ($)</label>
                    <input type="number" id="productPrice" required 
                           style="width: 100%; padding: 15px; background: rgba(255,255,255,0.05);
                                  border: 2px solid rgba(255,255,255,0.1); border-radius: 15px;
                                  color: white; font-family: 'Cairo'; font-size: 16px;"
                           placeholder="مثلاً: 499.99" step="0.01" min="0">
                </div>
                
                <button type="submit" class="btn-kawaghed" style="width: 100%; margin-top: 20px;">
                    🎉 نشر في كواغد
                </button>
                <button type="button" class="btn-kawaghed" onclick="closeModal()"
                        style="width: 100%; margin-top: 10px; background: rgba(255,255,255,0.1);">
                    ❌ إلغاء
                </button>
            </form>
        </div>
    </div>
    
    <script src="assets/js/app.js"></script>
</body>
</html>'''
    
    def generate_service_worker(self) -> str:
        """توليد Service Worker للتطبيق"""
        return '''const CACHE_NAME = 'kawaghed-store-v3';
const ASSETS = [
    '/',
    '/index.html',
    '/assets/css/style.css',
    '/assets/js/app.js',
    '/manifest.json'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => cache.addAll(ASSETS))
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then(keys => 
            Promise.all(
                keys.filter(key => key !== CACHE_NAME)
                    .map(key => caches.delete(key))
            )
        )
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then(response => response || fetch(event.request))
    );
});'''
    
    def generate_manifest(self) -> str:
        """توليد ملف manifest.json"""
        manifest = {
            "name": "متجر كواغد",
            "short_name": "كواغد",
            "description": self.config.slogan,
            "start_url": "/",
            "display": "standalone",
            "background_color": "#0a0a1a",
            "theme_color": self.config.primary_color,
            "orientation": "any",
            "icons": [
                {
                    "src": "data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🔥</text></svg>",
                    "sizes": "100x100",
                    "type": "image/svg+xml"
                }
            ]
        }
        return json.dumps(manifest, ensure_ascii=False, indent=2)
    
    def generate_all(self):
        """توليد جميع الملفات"""
        print("🔥 بدء توليد متجر كواغد...")
        print("═" * 50)
        
        self.create_directory_structure()
        
        # توليد CSS
        css = self.css_gen.generate_advanced_css(self.config)
        with open('assets/css/style.css', 'w', encoding='utf-8') as f:
            f.write(css)
        self.files_created.append('assets/css/style.css')
        print("✅ CSS تم توليد")
        
        # توليد JavaScript
        js = self.js_gen.generate_advanced_js(self.config)
        with open('assets/js/app.js', 'w', encoding='utf-8') as f:
            f.write(js)
        self.files_created.append('assets/js/app.js')
        print("✅ JavaScript تم توليد")
        
        # توليد HTML
        html = self.generate_html()
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        self.files_created.append('index.html')
        print("✅ HTML تم توليد")
        
        # توليد Service Worker
        with open('sw.js', 'w', encoding='utf-8') as f:
            f.write(self.generate_service_worker())
        self.files_created.append('sw.js')
        print("✅ Service Worker تم توليد")
        
        # توليد manifest.json
        with open('manifest.json', 'w', encoding='utf-8') as f:
            f.write(self.generate_manifest())
        self.files_created.append('manifest.json')
        print("✅ Manifest تم توليد")
        
        # توليد ملف الإعدادات
        config_data = asdict(self.config)
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(config_data, f, ensure_ascii=False, indent=4)
        self.files_created.append('config.json')
        print("✅ Config تم توليد")
        
        print("═" * 50)
        print("🔥 متجر كواغد جاهز للإطلاق!")
        print(f"📁 {len(self.files_created)} ملف تم إنشاؤه")
        for file in self.files_created:
            print(f"  ✅ {file}")

# ═══════════════════════════════════════════════════════════════
# دوال مساعدة للألوان
# ═══════════════════════════════════════════════════════════════

def _lighten_color(hex_color: str, factor: float = 0.2) -> str:
    """تفتيح اللون"""
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    r = min(255, int(r + (255 - r) * factor))
    g = min(255, int(g + (255 - g) * factor))
    b = min(255, int(b + (255 - b) * factor))
    return f'#{r:02x}{g:02x}{b:02x}'

def _darken_color(hex_color: str, factor: float = 0.2) -> str:
    """تعتيم اللون"""
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    r = max(0, int(r * (1 - factor)))
    g = max(0, int(g * (1 - factor)))
    b = max(0, int(b * (1 - factor)))
    return f'#{r:02x}{g:02x}{b:02x}'

# إضافة الدوال إلى الكلاس
StoreConfig._lighten_color = staticmethod(_lighten_color)
StoreConfig._darken_color = staticmethod(_darken_color)

# ═══════════════════════════════════════════════════════════════
# نقطة البداية
# ═══════════════════════════════════════════════════════════════

def main():
    generator = KawaghedStoreGenerator()
    generator.generate_all()
    
    # عرض إحصائيات
    print("\n📊 إحصائيات متجر كواغد:")
    print(f"   • Cloudinary: {generator.config.clouding_name}")
    print(f"   • Upload Preset: {generator.config.upload_preset}")
    print(f"   • رمز التفعيل: {generator.config.security_code}")
    print(f"   • الإصدار: {generator.config.version}")

if __name__ == "__main__":
    main()
