import streamlit as st
import base64
from streamlit_extras.switch_page_button import switch_page

def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(page_title="Transform Zone", page_icon="logo.png", layout="wide")

# --- STYLE FIX ---
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
    margin-top: 100px; /* Adjust for header height */
}

/* Hide sidebar ONLY on Home */
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
}

header, [data-testid="stHeader"] {
    display: none !important;
}

/* --- HEADER NAVIGATION --- */
.fixed-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 10000;
    background-color: #1a1a1a;
    padding: 16px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #333;
}

.fixed-header .nav-left, .nav-right {
    display: flex;
    gap: 25px;
    align-items: center;
}

.nav-btn {
    font-weight: 600;
    font-size: 1.2rem;
    padding: 8px 18px;
    border-radius: 6px;
    background: none;
    border: 1px solid transparent;
    color: white;
    cursor: pointer;
}

.nav-btn:hover {
    border-color: #5e60ce;
    color: #5e60ce;
}

.nav-highlight {
    color: #c59d41;
    font-weight: 700;
    text-shadow: 0 0 2px #c59d41;
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

logo_base64 = get_logo_base64()

# --- HEADER NAVIGATION ---
st.markdown(f"""
<div class="fixed-header">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" width="50">
        <button class="nav-btn" onclick="window.location.href='/'">Home</button>
        <button class="nav-btn" onclick="window.location.href='/Calculator'">Calculator</button>
        <button class="nav-btn" onclick="window.location.href='/Meals'">Meals</button>
        <button class="nav-btn" onclick="window.location.href='/Supplements'">Supplements</button>
    </div>
    <div class="nav-highlight">🔥 Get 20% Off Meal Plans!</div>
    <div class="nav-right">
        <button class="nav-btn" onclick="window.location.href='/Premium'">Premium</button>
        <button class="nav-btn" onclick="window.location.href='/Login'">Login</button>
    </div>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown("""
<div class="hero-img" style="background-image: url('https://images.unsplash.com/photo-1605296867304-46d5465a13f1'); background-size: cover; background-position: center; height: 700px; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding-top: 50px;">
    <h1 style="font-size: 4.5rem; font-weight: 700; text-shadow: 0px 0px 10px rgba(0,0,0,0.75);">Transform Zone</h1>
    <p style="font-size: 1.5rem; max-width: 850px; text-shadow: 0px 0px 10px rgba(0,0,0,0.75);">Your personal fitness companion — reach your goals faster with next-gen fitness tools designed for nutrition, performance, and recovery.</p>
    <a href="/Login" class="cta-button" style="background-color: #5e60ce; padding: 18px 42px; border-radius: 8px; color: #ffffff; font-size: 1.3rem; font-weight: 600; text-decoration: none; margin-top: 25px; box-shadow: 0px 4px 12px rgba(0,0,0,0.3);">Get Started</a>
</div>
""", unsafe_allow_html=True)
