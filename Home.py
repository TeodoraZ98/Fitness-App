import streamlit as st
import base64
from streamlit_extras.switch_page_button import switch_page


def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


st.set_page_config(page_title="Transform Zone", page_icon="logo.png", layout="wide")

# Hide sidebar ONLY on Home page
st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="collapsedControl"] {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- Theme ---
st.markdown("""
<style>
html, body {
    background-color: #000000 !important;
    color: #ffffff;
    font-family: 'Segoe UI', sans-serif;
}

[data-testid="stAppViewContainer"] > .main,
[data-testid="stMainBlockContainer"],
[data-testid="stAppViewBlockContainer"] {
    background-color: #000000 !important;
}

header, [data-testid="stHeader"] {
    display: none !important;
}

.main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 30px;
}

/* --- HEADER --- */
.custom-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 40px;
    background-color: #1a1a1a;
    border-bottom: 1px solid #333;
    font-size: 1.3rem;
    font-weight: 600;
    z-index: 999;
}
.nav-group {
    display: flex;
    gap: 20px;
    align-items: center;
}
.nav-btn {
    background: none;
    color: white;
    border: none;
    font-weight: 600;
    cursor: pointer;
    transition: color 0.2s ease;
}
.nav-btn:hover {
    color: #5e60ce;
}
.nav-highlight {
    color: #c59d41;
    font-weight: 700;
    text-shadow: 0 0 2px #c59d41;
}

/* --- HERO --- */
.hero-img {
    background-image: url('https://images.unsplash.com/photo-1605296867304-46d5465a13f1');
    background-size: cover;
    background-position: center;
    height: 700px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    text-shadow: 0px 0px 10px rgba(0,0,0,0.75);
    padding: 0 20px;
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
.feature-columns {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    justify-content: center;
    margin-top: 60px;
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
.feature-card p {
    font-size: 1.2rem;
    color: #cccccc;
}
.feature-card a {
    color: #5e60ce;
    text-decoration: none;
}
.feature-card a:hover {
    color: #7c7ef3;
}

/* --- FOOTER --- */
.footer {
    background-color: #1a1a1a;
    padding: 30px 40px;
    margin-top: 60px;
    border-top: 1px solid #333;
    color: #aaaaaa;
    font-size: 0.95rem;
    text-align: center;
}
.footer a {
    color: #5e60ce;
    text-decoration: none;
}
.footer a:hover {
    color: #7c7ef3;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = get_logo_base64()

# --- HEADER ---
st.markdown(f"""
<div class="custom-nav">
    <div class="nav-group">
        <img src="data:image/png;base64,{logo_base64}" width="50">
        <button class="nav-btn" onclick="window.location.href='/Home'">Home</button>
        <button class="nav-btn" onclick="window.location.href='/Calculator'">Calculator</button>
        <button class="nav-btn" onclick="window.location.href='/Meals'">Meals</button>
        <button class="nav-btn" onclick="window.location.href='/Supplements'">Supplements</button>
    </div>
    <div class="nav-highlight">🔥 Get 20% Off Meal Plans!</div>
    <div class="nav-group">
        <button class="nav-btn" onclick="window.location.href='/Premium'">Premium</button>
        <button class="nav-btn" onclick="window.location.href='/Login'">Login</button>
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
<div class="main-content">
    <div class="feature-columns">
        <div class="feature-card">
            <h4><a href="/Calculator">Macro & Calorie Calculators</a></h4>
            <p>Set your goals and determine how much protein, fat, and carbs you need each day.</p>
        </div>
        <div class="feature-card">
            <h4><a href="/Meals">Personalized Meal Plans</a></h4>
            <p>Smart meals calculated using your TDEE — powered by Spoonacular API.</p>
        </div>
        <div class="feature-card">
            <h4><a href="/Supplements">Supplement Recommendations</a></h4>
            <p>Get evidence-based suggestions to enhance your performance and recovery.</p>
        </div>
        <div class="feature-card">
            <h4><a href="/Premium">Premium Access</a></h4>
            <p>Unlock guides, macro history, downloads and personalized support.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    <p><strong>Contact Us:</strong> support@transformzone.com | +1 234 567 8901</p>
    <p>© 2025 Transform Zone. All rights reserved.
    <a href="/Privacy">Privacy Policy</a> |
    <a href="/Terms">Terms of Service</a></p>
</div>
""", unsafe_allow_html=True)
