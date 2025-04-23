import streamlit as st
import base64

def get_logo_base64(path="logo.png"):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def inject_custom_css(hide_sidebar=False):
    css = f"""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], .main {{
        background-color: #000000 !important;
        color: #ffffff !important;
        font-family: 'Segoe UI', sans-serif;
    }}
    [data-testid="stSidebar"] {{
        {"display: none !important;" if hide_sidebar else "background-color: #1a1a1a !important;"}
    }}
    [data-testid="collapsedControl"], header, [data-testid="stHeader"] {{
        display: none !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def handle_logout():
    query_params = st.query_params
    if "logout" in query_params:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_set_query_params()  # optional: clean URL
        st.switch_page("/Login")


def build_navbar(active_page=""):
    logo_base64 = get_logo_base64()
    logged_in = st.session_state.get("logged_in", False)

    nav_right = f"""
    <div class="nav-right">
        <a href="/Premium" target="_self">Premium</a>
        {"<a href='/?logout=true'>Logout</a>" if logged_in else "<a href='/Login' target='_self'>Login</a>"}
    </div>
    """

    st.markdown(f"""
    <div class="nav-container">
        <div class="nav-left">
            <img src="data:image/png;base64,{logo_base64}" class="nav-logo">
            <a href="/Home" target="_self" class="{ 'active' if active_page == 'Home' else '' }">Home</a>
            <a href="/Calculator" target="_self" class="{ 'active' if active_page == 'Calculator' else '' }">Calculator</a>
            <a href="/Meals" target="_self" class="{ 'active' if active_page == 'Meals' else '' }">Meals</a>
            <a href="/Supplements" target="_self" class="{ 'active' if active_page == 'Supplements' else '' }">Supplements</a>
        </div>
        <div class="nav-center">
            <a href="/Premium" target="_self">🔥 Get 20% Off Meal Plans!</a>
        </div>
        {nav_right}
    </div>
    """, unsafe_allow_html=True)
