import streamlit as st
import requests
from base64 import b64encode
from streamlit_cookies_manager import EncryptedCookieManager
from auth import generate_meal_plan


# --- PAGE CONFIG ---
st.set_page_config(page_title="Meal Suggestions", page_icon="logo.png", layout="wide")
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

# --- COOKIE SETUP ---
cookies = EncryptedCookieManager(password="supersecret123")
if not cookies.ready():
    st.stop()

if cookies.get("logged_in") == "true":
    st.session_state["logged_in"] = True
    st.session_state["username"] = cookies.get("username")

if "logged_in" not in st.session_state:
    st.warning("Please log in to view personalized meals.")
    st.stop()

if cookies.get("is_premium") == "true":
    st.session_state["is_premium"] = True

# --- LOAD LOGO ---
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# --- STYLING ---
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
.form-container {{
    font-size: 1.1rem;
    max-width: 500px;
    margin: 0 auto;
}}

.form-container select,
.form-container input {{
    font-size: 1rem;
    border-radius: 8px !important;
    background-color: #f5f5f5 !important;
    color: #000 !important;
}}

div.stButton > button:first-child {{
    background-color: #c59d41 !important;
    color: white !important;
    font-weight: bold !important;
    border: none !important;
    padding: 0.6rem 1.2rem !important;
    border-radius: 6px !important;
    transition: all 0.3s ease;
}}

div.stButton > button:first-child:hover {{
    background-color: #b2892f !important;
    transform: scale(1.03);
}}



label[data-testid="stWidgetLabel"] {{
    color: white !important;
    font-weight: 600 !important;
}}

div[data-testid="stAlertContainer"] {{
    background-color: rgba(255, 255, 255, 0.05) !important; /* subtle transparent light gray */
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 8px;
    padding: 1rem;
    color: #ccc !important;
}}

div[data-testid="stAlertContainer"] p {{
    color: #ccc !important;
    font-weight: 600;
}}

            
div[data-testid="stMainBlockContainer"] {{
    max-width: 1000px;
    margin: 0 auto;
}}

</style>

<!-- Navbar HTML -->
<div class="nav-container">
    <div class="nav-left">
        <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
        <a href="/" target="_self">Home</a>
        <a href="/Calculator" target="_self">Calculator</a>
        <a href="/Meals" target="_self" class="active">Meals</a>
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
st.markdown('<h1>Meal Suggestions</h1>', unsafe_allow_html=True)

# --- FORM CONTENT ---
with st.container():
    st.markdown('<div class="form-container">', unsafe_allow_html=True)

    goal = st.selectbox("Select your goal", ["Lose Fat", "Maintain", "Build Muscle"])
    st.info("Meals are based on your selected goal and fetched from Spoonacular.")

    API_KEY = "e33e933d9cff492eb5a92add23e35638"
    GOAL_CALORIES = {
        "Lose Fat": 1800,
        "Maintain": 2200,
        "Build Muscle": 2700
    }
    calories = GOAL_CALORIES[goal]

    url = f"https://api.spoonacular.com/mealplanner/generate?timeFrame=day&targetCalories={calories}&apiKey={API_KEY}"

    if st.button("Get Meal Plan"):
        with st.spinner("Fetching meal plan..."):
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                meals = data.get("meals", [])
                nutrients = data.get("nutrients", {})

                st.subheader("📊 Daily Overview")
                st.write(f"**Calories:** {nutrients.get('calories')} kcal | **Protein:** {nutrients.get('protein')} | **Fat:** {nutrients.get('fat')} | **Carbs:** {nutrients.get('carbohydrates')}")

                for meal in meals:
                    st.markdown("---")
                    st.subheader(meal["title"])
                    st.write(f"Ready in **{meal['readyInMinutes']}** minutes | Servings: **{meal['servings']}**")
                    st.markdown(f"[View Recipe →](https://spoonacular.com/recipes/{meal['title'].replace(' ', '-')}-{meal['id']})")
            else:
                st.error("Failed to fetch meals. Try again or check your API key.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- AI MEAL PLAN GENERATOR ---
st.markdown("---")  # visual divider
st.markdown("### 🤖 AI-Powered Meal Generator")

user_prompt = st.text_area("Enter a goal or request:",
                           placeholder="e.g. 1800 kcal vegetarian meal plan for fat loss")

if st.button("Generate with AI"):
    if user_prompt.strip():
        with st.spinner("Generating meal plan..."):
            ai_meal_plan = generate_meal_plan(user_prompt)
            st.markdown(ai_meal_plan)
    else:
        st.warning("Please enter a prompt.")
