import streamlit as st
import base64

def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


st.set_page_config(page_title="Transform Zone", page_icon="logo.png", layout="wide")
# ✅ Fix flash — force dark background before any render
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], .main {
    background-color: #000000 !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ✅ Then apply your custom design CSS
from theme import inject_custom_css
inject_custom_css()

# --- Custom CSS Styling ---
st.markdown("""
<style>
html, body {
    background-color: #000000 !important;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] > .main {
    background-color: #000000 !important;
}
[data-testid="stMainBlockContainer"] {
    background-color: #000000 !important;
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin-top: 40px;
}
[data-testid="stAppViewBlockContainer"] {
    background-color: #000000 !important;
}

/* --- NAVIGATION --- */
.nav-container {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1a1a1a;
    padding: 14px 40px;
    font-size: 1.7rem;
    font-weight: 600;
    border-bottom: 1px solid #333;
    z-index: 9999;
}

.nav-left, .nav-right {
    display: flex;
    gap: 20px;
    align-items: center;
}

.nav-left a, .nav-right a {
    text-decoration: none;
    color: #ffffff;
    transition: color 0.2s ease-in-out;
}

.nav-left a:hover, .nav-right a:hover {
    color: #5e60ce;
}

.nav-left .active, .nav-right .active {
    color: #5e60ce;
    border-bottom: 2px solid #5e60ce;
}

/* Logo image */
.nav-logo {
    height: 60px;
    width: auto;
    margin-right: 5px;
}

/* Center promo */
.nav-center {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    white-space: nowrap;
}

.nav-center a {
    font-weight: 700;
    color: #c59d41; /* same as logo */
    font-size: 1.3rem;
    text-decoration: none;
    text-shadow: 0 0 2px #c59d41;
    transition: all 0.3s ease-in-out;
}

.nav-center a:hover {
    color: #dcb86e;
    text-shadow: 0 0 6px #dcb86e;
}


/* --- HERO SECTION --- */
.hero-img {
    background-image: url('https://images.unsplash.com/photo-1605296867304-46d5465a13f1');
    background-size: cover;
    background-position: left -110px center;
    height: 700px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    color: white;
    text-shadow: 0px 0px 10px rgba(0,0,0,0.75);
    padding-top: 200px; 
}

.hero-img h1 {
    font-size: 4.5rem;
    font-weight: 700;
    margin-bottom: 20px;
}

.hero-img p {
    font-size: 1.5rem;
    margin-bottom: 35px;
    max-width: 850px;
    text-align: center;
}

.cta-button {
    background-color: #5e60ce;
    padding: 18px 42px;
    border-radius: 8px;
    color: #ffffff !important;
    font-size: 1.3rem;
    font-weight: 600;
    text-decoration: none;
    transition: background-color 0.3s ease-in-out;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.cta-button:hover {
    background-color: #4a4cc7;
}

/* --- FEATURES --- */
.section-header {
    font-size: 2rem;
    margin-top: 50px;
    margin-bottom: 20px;
    color: #ffffff;
    font-weight: 600;
    padding-left: 15px;
}

.outer-feature-container {
    background-color: #000000;
    padding: 40px 20px;
    margin-top: 110px; /* ⬅️ bumped from 30px to 80px */
}

.feature-columns {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    justify-content: center;
}

.feature-card {
    background-color: #2b2b2b;
    border-radius: 12px;
    padding: 25px;
    width: 420px;
    box-shadow: 0px 2px 12px rgba(255,255,255,0.05);
    transition: all 0.3s ease-in-out;
}

.feature-card:hover {
    box-shadow: 0px 8px 24px rgba(255,255,255,0.1);
}

.feature-card h4 {
    font-size: 1.5rem;
    color: #ffffff;
    margin-bottom: 10px;
}

.feature-card a {
    color: #5e60ce;
    text-decoration: none;
}

.feature-card a:hover {
    color: #7c7ef3;
}

.feature-card p {
    font-size: 1.2rem;
    color: #cccccc;
}

/* --- FOOTER --- */
.footer {
    background-color: #1a1a1a;
    padding: 30px 40px;
    margin-top: 60px;
    border-top: 1px solid #333;
    color: #aaaaaa;
    font-size: 0.95rem;
}

.footer a {
    color: #5e60ce;
    text-decoration: none;
}

.footer a:hover {
    color: #7c7ef3;
}

/* --- Hide Sidebar + Collapsed Arrow --- */
[data-testid="stSidebar"] {
    display: none;
}

[data-testid="collapsedControl"] {
    display: none !important;
}
            
header, [data-testid="stHeader"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = get_logo_base64()


# --- HEADER NAVIGATION ---
st.markdown(f"""
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" target="_self" class="active">Home</a>
        <a href="/Calculator" target="_self">Calculator</a>
        <a href="/Meals" target="_self">Meals</a>
        <a href="/Supplements" target="_self">Supplements</a>
    </div>
    <div class="nav-center">
        <a href="/Premium" target="_self">🔥 Get 20% Off Meal Plans!</a>
    </div>
    <div class="nav-right">
        <a href="/Premium" target="_self">Premium</a>
        <a href="/Login" target="_self">Login</a>
    </div>
</div>
""", unsafe_allow_html=True)




# --- HERO SECTION ---
st.markdown("""
<div class="hero-img">
    <h1>Transform Zone</h1>
    <p>Your personal fitness companion — reach your goals faster with next-gen fitness tools designed for nutrition, performance, and recovery.</p>
    <a href="/Login" class="cta-button">Get Started</a>
</div>
""", unsafe_allow_html=True)

# --- FEATURES ---
st.markdown("""
<div class="outer-feature-container">
    <div class="feature-columns">
        <div class="feature-card">
            <h4> <a href="/Calculator" target="_self">Macro & Calorie Calculators</a></h4>
            <p>Set your goals and determine how much protein, fat, and carbs you need each day.</p>
        </div>
        <div class="feature-card">
            <h4> <a href="/Meals" target="_self">Personalized Meal Plans</a></h4>
            <p>Smart meals calculated using your TDEE — powered by Spoonacular API.</p>
        </div>
        <div class="feature-card">
            <h4> <a href="/Supplements" target="_self">Supplement Recommendations</a></h4>
            <p>Get evidence-based suggestions to enhance your performance and recovery.</p>
        </div>
        <div class="feature-card">
            <h4> <a href="/Premium" target="_self">Premium Access</a></h4>
            <p>Unlock guides, macro history, downloads and personalized support.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- LOGIN STATUS ---
st.markdown("<hr style='margin-top: 40px;'>", unsafe_allow_html=True)

if "logged_in" in st.session_state:
    username = st.session_state["username"].capitalize()
    st.markdown(f"""
    <div style="background-color: rgba(0, 80, 0, 0.4); padding: 16px 20px; border-radius: 10px; color: #d4ffd4; font-size: 1.1rem; display: flex; align-items: center; justify-content: space-between;">
        ✅ Logged in as: <strong style="color: #c6ffc6;">{username}</strong>
        <span style="margin-left: auto;">
            <span style="color: #dddddd;">Want to switch accounts?</span>
            <a href="/?logout=true" style="color: #ff6666; font-weight: 600; text-decoration: none; margin-left: 10px;">
                🔓 Log out
            </a>
        </span>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; margin-bottom: 50px;'>
        <a href='/Login' target='_self' style='font-size: 1.6rem; color: #5e60ce; font-weight: bold; text-decoration: none; background-color: #1a1a1a; padding: 16px 32px; border-radius: 10px; box-shadow: 0px 4px 15px rgba(94,96,206,0.4); transition: background-color 0.3s ease;'>
            🔐 Unlock Your Personalized Fitness Plan — Join Now
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p><strong>Contact Us:</strong> support@transformzone.com | +1 234 567 8901</p>
    <p>© 2025 Transform Zone. All rights reserved.
    <a href="/Privacy" target="_self">Privacy Policy</a> |
    <a href="/Terms" target="_self">Terms of Service</a></p>
</div>
""", unsafe_allow_html=True)

