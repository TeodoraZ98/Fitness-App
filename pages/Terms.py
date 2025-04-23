import streamlit as st
from base64 import b64encode
from streamlit_cookies_manager import EncryptedCookieManager

st.set_page_config(page_title="Terms of Service", page_icon="📜", layout="wide")
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

cookies = EncryptedCookieManager(password="supersecret123")
if not cookies.ready():
    st.stop()

# --- RESTORE SESSION ---
if cookies.get("logged_in") == "true":
    st.session_state["logged_in"] = True
    st.session_state["username"] = cookies.get("username")
    
if cookies.get("is_premium") == "true":
    st.session_state["is_premium"] = True

# Load logo
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# --- CUSTOM CSS & NAVBAR ---
st.markdown(f"""
<style>
@media (min-width: 768px) {{
    [data-testid="stSidebar"] {{
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        z-index: 998;
    }}
    [data-testid="stAppViewContainer"] > .main {{
        margin-left: 18rem;
    }}
}}

[data-testid="stAppViewContainer"] > .main,
[data-testid="stMainBlockContainer"],
[data-testid="stAppViewBlockContainer"],
[data-testid="stMain"] {{
    background-color: #000 !important;
    color: white;
    font-family: 'Segoe UI', sans-serif;
    padding-top: 20px;
}}

header, [data-testid="stHeader"] {{
    display: none !important;
}}

/* Sidebar */
[data-testid="stSidebarContent"] {{
    background-color: #121212 !important;
    color: white !important;
}}

[data-testid="stSidebarContent"] * {{
    color: white !important;
}}

[data-testid="stSidebar"] a:hover {{
    color: #5e60ce !important;
}}

[data-testid="stSidebar"] a[href*="Privacy"],
[data-testid="stSidebar"] a[href*="Terms"] {{
    display: none !important;
}}

[data-testid="stSidebar"] a[href$="/Login"] {{
    margin-top: 120px;
    display: block;
}}

button[title="Hide sidebar"] svg,
button[title="Show sidebar"] svg {{
    color: white !important;
    stroke: white !important;
}}

/* Navbar */
.nav-container {{
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: #1a1a1a;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 40px;
    font-size: 1.2rem;
    z-index: 999;
    border-bottom: 1px solid #333;
}}

.nav-left, .nav-center, .nav-right {{
    display: flex;
    align-items: center;
    gap: 35px;
}}

.nav-logo {{
    height: 32px;
}}

.nav-left a, .nav-right a {{
    color: white;
    text-decoration: none;
    font-weight: 600;
}}

.nav-left a.active {{
    border-bottom: 2px solid #5e60ce;
}}

.nav-left a:hover, .nav-right a:hover {{
    color: #5e60ce;
}}

.nav-center a {{
    color: #d4a017;
    font-weight: 700;
    text-shadow: 0 0 6px rgba(255, 204, 0, 0.6);
    text-decoration: none;
}}

.nav-center a:hover {{
    text-shadow: none;
    color: #5e60ce;
}}

/* Title and content */
h1 {{
    font-size: 2.6rem;
    font-weight: 700;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}}

.markdown-content {{
    max-width: 700px;
    margin: 0 auto;
    font-size: 1.05rem;
}}

.markdown-content h3 {{
    margin-top: 1.6rem;
    color: #d4a017;
}}

.markdown-content ul {{
    margin-bottom: 1.5rem;
}}

strong {{
    color: white !important;
}}
</style>

<!-- Navbar -->
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" target="_self">Home</a>
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

# --- TITLE ---
st.markdown('<h1>Terms of Service</h1>', unsafe_allow_html=True)

# --- CONTENT ---
st.markdown("""
<div class="markdown-content">

### 1. Use of Service
You agree to use Transform Zone only for lawful purposes...

### 2. Account Responsibility
You are responsible for maintaining the confidentiality of your login credentials...

### 3. Changes to Terms
We may update these Terms from time to time. We’ll notify you of major changes.

---

📩 For more questions, contact: [support@transformzone.com](mailto:support@transformzone.com)

</div>
""", unsafe_allow_html=True)
