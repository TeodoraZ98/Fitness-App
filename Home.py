import streamlit as st
import base64
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Transform Zone", page_icon="logo.png", layout="wide")

def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# ✅ Hide sidebar on Home only
st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)


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

[data-testid="stMainBlockContainer"] {
    background-color: #000000 !important;
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin-top: 100px;
}

/* --- HEADER --- */
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
    font-size: 1.3rem;
    font-weight: 600;
    border-bottom: 1px solid #333;
    z-index: 9999;
}
.nav-left, .nav-right {
    display: flex;
    gap: 20px;
    align-items: center;
}
.nav-link {
    background: none;
    color: white;
    border: none;
    font-weight: 600;
    cursor: pointer;
    font-size: 1.2rem;
    transition: color 0.2s ease;
}
.nav-link:hover {
    color: #5e60ce;
}
.nav-center {
    font-weight: 700;
    color: #c59d41;
    font-size: 1.1rem;
    text-shadow: 0 0 2px #c59d41;
}

/* --- HERO --- */
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
</style>
""", unsafe_allow_html=True)

# --- HEADER NAVIGATION ---
logo_base64 = get_logo_base64()
col1, col2, col3 = st.columns([2, 2, 1.5])
with col1:
    st.markdown(f"<div class='nav-container'><div class='nav-left'><img src='data:image/png;base64,{logo_base64}' height='40'>", unsafe_allow_html=True)
    if st.button("Home", key="nav_home", help="Go to Home", use_container_width=True):
        switch_page("Home")
    if st.button("Calculator", key="nav_calc", use_container_width=True):
        switch_page("Calculator")
    if st.button("Meals", key="nav_meals", use_container_width=True):
        switch_page("Meals")
    if st.button("Supplements", key="nav_supp", use_container_width=True):
        switch_page("Supplements")
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='nav-center'>🔥 Get 20% Off Meal Plans!</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='nav-right'>", unsafe_allow_html=True)
    if st.button("Premium", key="nav_premium", use_container_width=True):
        switch_page("Premium")
    if st.button("Login", key="nav_login", use_container_width=True):
        switch_page("Login")
    st.markdown("</div></div>", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-img">
    <h1>Transform Zone</h1>
    <p>Your personal fitness companion — reach your goals faster with next-gen fitness tools designed for nutrition, performance, and recovery.</p>
    <a href="/Login" class="cta-button">Get Started</a>
</div>
""", unsafe_allow_html=True)

# --- FEATURES SECTION (same as before) ---
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
