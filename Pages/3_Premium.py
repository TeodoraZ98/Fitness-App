import streamlit as st
import pandas as pd
import requests
import io
from base64 import b64encode
from reportlab.pdfgen import canvas
from database import connect_db
from streamlit_cookies_manager import EncryptedCookieManager

st.set_page_config(page_title="Premium Content", page_icon="logo.png", layout="wide")

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

# Load logo
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# --- COOKIE SETUP ---
cookies = EncryptedCookieManager(password="supersecret123")
if not cookies.ready():
    st.stop()

# --- RESTORE SESSION ---
if cookies.get("logged_in") == "true":
    st.session_state["logged_in"] = True
    st.session_state["username"] = cookies.get("username")

if cookies.get("is_premium") == "true":
    st.session_state["is_premium"] = True

# --- STYLE & NAV ---
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

.subheader {{
    font-size: 1.6rem;
    font-weight: 600;
    margin-top: 2.5rem;
    color: #d4a017;
}}

.stAlertContainer, .stAlertContainer p {{
    background-color: #c59d41 !important;
    color: white !important;
    font-weight: bold !important;
}}

strong {{
    color: white !important;
}}

.stButton button {{
    background-color: #c59d41 !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 6px !important;
    transition: all 0.3s ease;
}}

.stButton button:hover {{
    background-color: #b2892f !important;
    transform: scale(1.03);
}}

/* Light grey, semi-transparent table */
div[data-testid="stDataFrame"] div[role="grid"] {{
    background-color: rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    padding: 0.5rem;
    box-shadow: 0 0 10px rgba(255, 255, 255, 0.05);
}}

div[data-testid="stDataFrame"] thead, 
div[data-testid="stDataFrame"] tbody, 
div[data-testid="stDataFrame"] tr, 
div[data-testid="stDataFrame"] td {{
    background-color: transparent !important;
    color: white !important;
    font-size: 0.95rem;
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
         

div[data-testid="stForm"] button {{
    background-color: #c59d41 !important; 
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 6px !important;
    transition: all 0.3s ease;
}}

div[data-testid="stForm"] button:hover {{
    background-color: #b2892f !important;
    transform: scale(1.03);
}}


/* Target the Streamlit form and limit width */
[data-testid="stForm"] {{
    max-width: 500px;
    margin: 0 auto !important;
    background-color: #0e0e0e;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 0 12px rgba(255, 255, 255, 0.05);
}}

/* Input field inside form */
[data-testid="stForm"] input {{
    max-width: 100% !important;
    border-radius: 8px !important;
}}

/* Make the button match form width */
[data-testid="stForm"] .stButton button {{
    width: 100% !important;
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
        <a href="/Premium" target="_self" class="active">🔥 Get 20% Off Meal Plans!</a>
    </div>
    <div class="nav-right">
        <a href="/Premium" target="_self" class="active">Premium</a>
        <a href="/Login" target="_self">Login</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PAGE TITLE ---
st.markdown('<h1>Premium Content</h1>', unsafe_allow_html=True)

# --- CHECK LOGIN ---
if "logged_in" not in st.session_state:
    st.warning("Please log in to view premium content.")
    st.stop()

# --- IF NOT PREMIUM, ASK FOR CODE ---
if not st.session_state.get("is_premium"):
    with st.container():
        st.markdown('<div class="form-wrapper">', unsafe_allow_html=True)

        with st.form("unlock_form"):
            st.subheader("🔑 Enter Premium Code to Unlock")
            code = st.text_input("Premium Code")
            unlock = st.form_submit_button("Unlock")

            if unlock:
                if code == "FITPREMIUM2024":
                    conn = connect_db()
                    c = conn.cursor()
                    c.execute("UPDATE users SET is_premium = 1 WHERE username = ?", (st.session_state["username"],))
                    conn.commit()
                    conn.close()

                    cookies["is_premium"] = "true"
                    cookies.save()
                    st.session_state["is_premium"] = True
                    st.experimental_rerun()
                else:
                    st.error("🚫 Invalid premium code.")

        st.markdown('</div>', unsafe_allow_html=True)

    st.stop()


# --- MACRO HISTORY ---
st.markdown('<div class="subheader">Your Macro Calculator History</div>', unsafe_allow_html=True)

conn = connect_db()
c = conn.cursor()
c.execute("""
    SELECT date, tdee, protein, fat, carbs
    FROM calculations
    WHERE username = ?
    ORDER BY date DESC
""", (st.session_state["username"],))
rows = c.fetchall()
conn.close()

if rows:
    df = pd.DataFrame(rows, columns=["Date", "TDEE", "Protein (g)", "Fat (g)", "Carbs (g)"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("No past calculations found.")

# --- PREMIUM PERKS ---
st.markdown('<div class="subheader">Premium Perks</div>', unsafe_allow_html=True)
st.markdown("""
- ✅ Full macro history  
- ✅ Personalized meal planner  
- ✅ Download exact plan as PDF  
- ✅ Coaching access  
""")

# --- MEAL PLAN ---
st.markdown('<div class="subheader">Personalized Meal Plan</div>', unsafe_allow_html=True)

if rows:
    latest_tdee = rows[0][1]
    st.markdown(f"Generating meals for **{latest_tdee} kcal** target...")

    API_KEY = "e33e933d9cff492eb5a92add23e35638"
    url = f"https://api.spoonacular.com/mealplanner/generate?timeFrame=day&targetCalories={latest_tdee}&apiKey={API_KEY}"

    if st.button("Generate My Meal Plan"):
        with st.spinner("Fetching meals..."):
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                meals = data.get("meals", [])
                nutrients = data.get("nutrients", {})

                st.session_state["meal_plan"] = meals
                st.session_state["meal_nutrients"] = nutrients

                st.markdown("### 📊 Daily Nutrition Summary")
                st.write(
                    f"**Calories:** {nutrients.get('calories')} kcal | "
                    f"**Protein:** {nutrients.get('protein')} | "
                    f"**Fat:** {nutrients.get('fat')} | "
                    f"**Carbs:** {nutrients.get('carbohydrates')}"
                )

                for meal in meals:
                    st.markdown("---")
                    st.subheader(meal["title"])
                    st.write(f"Ready in {meal['readyInMinutes']} minutes | Servings: {meal['servings']}")
                    st.markdown(f"[View Recipe →](https://spoonacular.com/recipes/{meal['title'].replace(' ', '-')}-{meal['id']})")
            else:
                st.error("Error fetching meal plan. Check your API key or try again.")
else:
    st.info("You need at least one calculator result to generate a meal plan.")

# --- PDF GENERATOR ---
def generate_meal_plan_pdf():
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 800, "🍽️ Your Personalized Meal Plan")

    nutrients = st.session_state.get("meal_nutrients", {})
    p.setFont("Helvetica", 12)
    p.drawString(100, 780, f"Calories: {nutrients.get('calories', '')} kcal")
    p.drawString(100, 765, f"Protein: {nutrients.get('protein', '')}")
    p.drawString(100, 750, f"Fat: {nutrients.get('fat', '')}")
    p.drawString(100, 735, f"Carbs: {nutrients.get('carbohydrates', '')}")

    meals = st.session_state.get("meal_plan", [])
    y = 710
    for meal in meals:
        p.drawString(100, y, f"- {meal['title']} ({meal['readyInMinutes']} min | Servings: {meal['servings']})")
        y -= 20
        if y < 100:
            p.showPage()
            y = 800

    p.save()
    buffer.seek(0)
    return buffer

# --- DOWNLOAD BUTTON ---
if "meal_plan" in st.session_state:
    st.download_button(
        label="📥 Download This Meal Plan (PDF)",
        data=generate_meal_plan_pdf(),
        file_name="my_meal_plan.pdf",
        mime="application/pdf"
    )


