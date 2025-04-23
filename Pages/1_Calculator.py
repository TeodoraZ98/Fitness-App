import streamlit as st
from datetime import datetime
from database import connect_db
from base64 import b64encode
import matplotlib.pyplot as plt
from streamlit_cookies_manager import EncryptedCookieManager
import numpy as np
import plotly.graph_objects as go

from theme import inject_custom_css, build_navbar, handle_logout

st.set_page_config(page_title="Calculator", page_icon="logo.png", layout="wide")
handle_logout()
inject_custom_css()
build_navbar(active_page="Calculator")





cookies = EncryptedCookieManager(password="supersecret123")
if not cookies.ready():
    st.stop()


# Restore session from cookies if needed
if cookies.get("logged_in") == "true":
    st.session_state["logged_in"] = True
    st.session_state["username"] = cookies.get("username")

# Require login
if "logged_in" not in st.session_state:
    st.warning("Please log in to access this page.")
    st.stop()

if cookies.get("is_premium") == "true":
    st.session_state["is_premium"] = True
    
# Load logo
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# Inject CSS
st.markdown(f"""
<style>
/* General layout */
@media (min-width: 768px) {{
    [data-testid="stSidebar"] {{
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        z-index: 998;
        transition: all 0.3s ease;
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

/* Title */
h1 {{
    font-size: 2.6rem;
    font-weight: 700;
    color: white;
    text-align: center;
}}

/* Form styling */
div[data-testid="stForm"] {{
    font-size: 1.1rem;
    max-width: 500px;
    margin: 0 auto;
}}

div[data-testid="stForm"] input,
div[data-testid="stForm"] select {{
    font-size: 1rem;
    border-radius: 8px !important;
    background-color: #f5f5f5 !important;
    color: #000 !important;
}}

div[data-testid="stFormSubmitButton"] {{
    margin-top: 1rem;
    margin-bottom: 2rem;
}}

div[data-testid="stRadio"] > div[role="radiogroup"] > label > div {{
    color: white !important;
    font-weight: 500 !important;
}}

div[data-testid="stRadio"] label:hover div,
div[data-testid="stRadio"] input[type="radio"]:checked + div {{
    color: #f5f5f5 !important;
}}

div[data-testid="stFormSubmitButton"] button {{
    background-color: #c59d41 !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 6px !important;
    transition: all 0.3s ease;
}}

div[data-testid="stFormSubmitButton"] button:hover {{
    background-color: #b2892f !important;
    transform: scale(1.03);
}}

label[data-testid="stWidgetLabel"] {{
    color: white !important;
    font-weight: 600 !important;
}}

/* Fix alert success background to match the golden color */
div[data-testid="stAlertContainer"] {{
    background-color: #c59d41 !important;
    color: white !important;
}}

/* Optional: Adjust border or text if needed */
div[data-testid="stAlertContainer"] p {{
    color: white !important;
    font-weight: bold;
}}


[data-testid="stMetric"] div {{
    color: white !important;
}}

strong {{
    color: white !important;
}}
</style>

<!-- Navbar HTML -->
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" target="_self">Home</a>
        <a href="/Calculator" target="_self" class="active">Calculator</a>
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
st.title("Calorie & Macro Calculator")

# --- LOGIN CHECK ---
if "logged_in" not in st.session_state:
    st.warning("Please log in to use the calculator.")
    st.stop()

# --- INPUT FORM ---
with st.form("macro_calc"):
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    height = st.number_input("Height (cm)", min_value=100, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
    activity = st.selectbox("Activity Level", [
        "Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"
    ])
    goal = st.selectbox("Goal", ["Maintain", "Lose Fat", "Build Muscle"])
    submit = st.form_submit_button("Calculate")

# --- LOGIC ---
def calculate_tdee(gender, age, height, weight, activity):
    bmr = 10 * weight + 6.25 * height - 5 * age + (5 if gender == "Male" else -161)
    factors = {
        "Sedentary": 1.2, "Lightly active": 1.375, "Moderately active": 1.55,
        "Very active": 1.725, "Super active": 1.9
    }
    return round(bmr * factors[activity])

def calculate_macros(tdee, goal):
    if goal == "Lose Fat":
        tdee -= 500
    elif goal == "Build Muscle":
        tdee += 300
    protein = round((tdee * 0.3) / 4)
    fat = round((tdee * 0.25) / 9)
    carbs = round((tdee - (protein * 4 + fat * 9)) / 4)
    return tdee, protein, fat, carbs

# --- RESULTS ---
if submit:
    tdee = calculate_tdee(gender, age, height, weight, activity)
    tdee, protein, fat, carbs = calculate_macros(tdee, goal)

    st.success("Your results:")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown(f"<h3 style='text-align:center;'>TDEE</h3>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align:center; color:white;'>{tdee} kcal</h1>", unsafe_allow_html=True)
        st.markdown(f"""
            <p style='text-align:center; font-size:2.1rem;'>
            <strong>Protein:</strong> {protein}g<br>
            <strong>Fat:</strong> {fat}g<br>
            <strong>Carbs:</strong> {carbs}g
            </p>
        """, unsafe_allow_html=True)



    with col2:

        fig = go.Figure(data=[go.Pie(
            labels=['Protein', 'Fat', 'Carbs'],
            values=[protein, fat, carbs],
            hole=0.55,
            marker=dict(colors=['purple', 'orange', 'green']),
            textinfo='percent+label',
            insidetextorientation='radial',
            textfont=dict(size=14, color='white')
        )])

        fig.update_layout(
            showlegend=False,
            paper_bgcolor='black',
            plot_bgcolor='black',
            margin=dict(t=0, b=0, l=0, r=0),
            height=280,
        )
        st.plotly_chart(fig, use_container_width=False)





    # Save to DB
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS calculations (
            username TEXT,
            date TEXT,
            tdee INTEGER,
            protein INTEGER,
            fat INTEGER,
            carbs INTEGER
        )
    ''')
    c.execute("INSERT INTO calculations VALUES (?, ?, ?, ?, ?, ?)", (
        st.session_state["username"],
        datetime.now().strftime("%Y-%m-%d %H:%M"),
        tdee, protein, fat, carbs
    ))
    conn.commit()
    conn.close()
    st.success("Saved to your profile!")
