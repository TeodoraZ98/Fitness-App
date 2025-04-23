import streamlit as st
from database import create_users_table, add_user, get_user
from auth import hash_password, check_password
from streamlit_cookies_manager import EncryptedCookieManager
from base64 import b64encode

st.set_page_config(page_title="Login", page_icon="logo.png", layout="wide")

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

# --- DATABASE ---
create_users_table()

# --- LOAD LOGO ---
with open("logo.png", "rb") as f:
    logo_base64 = b64encode(f.read()).decode()

# --- STYLE + NAVBAR ---
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
    padding-top: 40px;
}}

header, [data-testid="stHeader"] {{
    display: none !important;
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

h1 {{
    font-size: 2.6rem;
    font-weight: 700;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}}

div[data-testid="stForm"] {{
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

div[data-testid="stAlertContainer"] {{
    background-color: #c59d41 !important;
    color: white !important;
}}

div[data-testid="stAlertContainer"] p {{
    color: white !important;
    font-weight: bold;
}}

[data-testid="stMarkdownContainer"] {{
    color: white !important;
    font-weight: 600;
}}
            
[data-testid="stRadio"] {{
    margin-left: 700px;
    margin-top: 20px;
    margin-bottom: 20px;
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
        <a href="/Login" target="_self" class="active">Login</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- PAGE TITLE ---
st.title("Login or Register")

# --- MODE SELECT ---
menu = st.radio("Choose an option", ["Login", "Register"])

# --- LOGIN FORM ---
if menu == "Login":
    with st.form("login_form"):
        st.subheader("Log In")
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")
        login_btn = st.form_submit_button("Login")

        if login_btn:
            user = get_user(username)
            if user:
                if check_password(password, user[3]):
                    st.success(f"Welcome back, {user[1]}!")
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = user[0]
                    st.session_state["is_premium"] = bool(user[4])
                    cookies["logged_in"] = "true"
                    cookies["username"] = user[0]
                    cookies["is_premium"] = "true" if user[4] else "false"
                    cookies.save()
                else:
                    st.error("Incorrect password.")
            else:
                st.error("User not found. Please register first.")

# --- REGISTER FORM ---
elif menu == "Register":
    with st.form("register_form"):
        st.subheader("Create a New Account")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        username = st.text_input("Username")
        email = st.text_input("Email")
        country = st.text_input("Country")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        register_btn = st.form_submit_button("Register")

        if register_btn:
            if all([first_name, last_name, username, email, country, phone, password]):
                if get_user(username):
                    st.error("Username already exists.")
                else:
                    full_name = f"{first_name} {last_name}"
                    add_user(username, full_name, email, hash_password(password))
                    st.success("Account created! You can now log in.")
            else:
                st.warning("Please fill out all fields.")
