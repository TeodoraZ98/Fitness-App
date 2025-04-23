import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
from base64 import b64encode
import io
from reportlab.pdfgen import canvas
from theme import inject_custom_css



st.set_page_config(page_title="Supplements", page_icon="logo.png", layout="wide")
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], .main {
    background-color: #000000 !important;
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

inject_custom_css()


# --- COOKIE SETUP ---
cookies = EncryptedCookieManager(password="supersecret123")
if not cookies.ready():
    st.stop()

if cookies.get("logged_in") == "true":
    st.session_state["logged_in"] = True
    st.session_state["username"] = cookies.get("username")

if cookies.get("is_premium") == "true":
    st.session_state["is_premium"] = True

if "logged_in" not in st.session_state:
    st.warning("Please log in to view personalized supplements.")
    st.stop()

# --- LOAD LOGO ---
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# --- CUSTOM CSS + NAVBAR ---
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

h1 {{
    font-size: 2.6rem;
    font-weight: 700;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}}

.download-container {{
    display: flex;
    justify-content: center;
    margin-top: 2rem;
}}

div[data-testid="stDownloadButton"] button {{
    background-color: #c59d41 !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 6px !important;
    transition: all 0.3s ease;
}}

div[data-testid="stDownloadButton"] button:hover {{
    background-color: #b2892f !important;
    transform: scale(1.03);
}}

</style>

<!-- Navbar -->
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" target="_self">Home</a>
        <a href="/Calculator" target="_self">Calculator</a>
        <a href="/Meals" target="_self">Meals</a>
        <a href="/Supplements" target="_self" class="active">Supplements</a>
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

# --- CONTENT ---
st.markdown("<h1>Supplement Recommendations</h1>", unsafe_allow_html=True)

st.markdown("""

### 🔹 General Fitness
- **Whey Protein:** Boosts protein intake for recovery and muscle maintenance.
- **Creatine Monohydrate:** Improves strength and endurance, especially for resistance training.
- **Multivitamin:** Covers basic micronutrient needs.

---

### 🔹 Fat Loss Support
- **Green Tea Extract:** May support fat oxidation.
- **Caffeine (if tolerated):** Boosts energy and helps control appetite.
- **L-Carnitine:** Supports fat metabolism.

---

### 🔹 Muscle Gain & Recovery
- **Creatine:** Backed by science for strength and size.
- **Beta-Alanine:** Helps buffer lactic acid during training.
- **Fish Oil (Omega-3):** Reduces inflammation, supports recovery.

---

> 💡 Always consult your physician or a certified coach before starting any supplement.
""")

# --- DOWNLOAD BUTTON ---
supplement_text = """
SUPPLEMENT GUIDE

General:
- Whey Protein
- Creatine Monohydrate
- Multivitamin

Fat Loss:
- Green Tea Extract
- Caffeine
- L-Carnitine

Muscle Gain:
- Creatine
- Beta-Alanine
- Omega-3
""".strip()

st.markdown('<div class="download-container">', unsafe_allow_html=True)

def generate_supplement_pdf():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, "💊 Supplement Guide")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 770, "General Fitness")
    p.setFont("Helvetica", 11)
    p.drawString(120, 755, "- Whey Protein")
    p.drawString(120, 740, "- Creatine Monohydrate")
    p.drawString(120, 725, "- Multivitamin")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 700, "Fat Loss Support")
    p.setFont("Helvetica", 11)
    p.drawString(120, 685, "- Green Tea Extract")
    p.drawString(120, 670, "- Caffeine")
    p.drawString(120, 655, "- L-Carnitine")

    p.setFont("Helvetica-Bold", 12)
    p.drawString(100, 630, "Muscle Gain & Recovery")
    p.setFont("Helvetica", 11)
    p.drawString(120, 615, "- Creatine")
    p.drawString(120, 600, "- Beta-Alanine")
    p.drawString(120, 585, "- Fish Oil (Omega-3)")

    p.setFont("Helvetica-Oblique", 10)
    p.drawString(100, 550, "💡 Always consult your physician or coach before starting supplements.")

    p.save()
    buffer.seek(0)
    return buffer

# --- Styled PDF Download Button ---
st.markdown('<div class="download-container">', unsafe_allow_html=True)
st.download_button(
    label="📥 Download This Supplement Guide (PDF)",
    data=generate_supplement_pdf(),
    file_name="supplement_guide.pdf",
    mime="application/pdf"
)

st.markdown('</div>', unsafe_allow_html=True)

st.info("✅ Use this guide alongside your nutrition and workout plan for best results.")
