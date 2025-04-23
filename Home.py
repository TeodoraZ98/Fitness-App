import streamlit as st
import base64

def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="Transform Zone", page_icon="logo.png", layout="wide")

# --- Fix flash background early ---
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], .main {
    background-color: #000000 !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# --- Load custom theme ---
from theme import inject_custom_css
inject_custom_css()

# --- Hide Sidebar & Header ---
st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"], header, [data-testid="stHeader"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = get_logo_base64()

# --- HEADER NAVIGATION ---
st.markdown(f"""
<style>
.nav-container {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #1a1a1a;
    padding: 14px 40px;
    font-size: 1.4rem;
    font-weight: 600;
    border-bottom: 1px solid #333;
    z-index: 9999;
}}
.nav-left, .nav-right {{
    display: flex;
    gap: 22px;
    align-items: center;
}}
.nav-logo {{
    height: 50px;
    margin-right: 10px;
}}
.nav-link {{
    color: white;
    text-decoration: none;
    transition: color 0.2s ease;
}}
.nav-link:hover {{
    color: #5e60ce;
}}
.nav-highlight {{
    color: #c59d41;
    font-weight: 700;
    text-shadow: 0 0 2px #c59d41;
    font-size: 1.1rem;
}}
</style>
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" class="nav-link">Home</a>
        <a href="/Calculator" class="nav-link">Calculator</a>
        <a href="/Meals" class="nav-link">Meals</a>
        <a href="/Supplements" class="nav-link">Supplements</a>
    </div>
    <div class="nav-highlight">🔥 Get 20% Off Meal Plans!</div>
    <div class="nav-right">
        <a href="/Premium" class="nav-link">Premium</a>
        <a href="/Login" class="nav-link">Login</a>
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
