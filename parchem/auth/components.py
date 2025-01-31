import streamlit as st
from .service import create_user, authenticate_user
from .service import check_session

def load_css():
    with open('parchem/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call the load_css function
load_css()

def show_login():
    """
    Display the login form.
    """
    with st.form("Login"):
        email = st.text_input("Email",key="email_input")
        password = st.text_input("Password", type="password",key="password_input")
        if st.form_submit_button("Login"):
            user = authenticate_user(email, password)
            if user:
                st.success("Logged in successfully!")
                st.rerun()

def show_signup():
    """
    Display the signup form.
    """
    with st.form("Signup"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        if st.form_submit_button("Sign Up"):
            if password == confirm_password:
                user = create_user(email, password)
                if user:
                    st.success("Account created successfully!")
                    st.rerun()
            else:
                st.error("Passwords do not match")


def show_login_prompt():
    """
    Display a login prompt if the user is not authenticated.
    Hide this prompt once the user logs in.
    """
    if not check_session():
        # Use a container to manage duplicate rendering
        with st.empty():
            st.markdown(
                """
                <div style="text-align: center; margin-top: 50px;">
                    <h3>Please login first to start chatting with </h3>
                    <h3><span class="animated-text">Parchem.ai</span><span class="dots"><span>.</span><span>.</span><span>.</span></span></h3>
                </div>
                """,
                unsafe_allow_html=True
            )


def display_logo():
    """
    Display the Parchem logo at the top center of the sidebar.
    """
    logo_url = "https://www.parchem.com/images/logo.svg"
    st.sidebar.markdown(
        f"""
        <div style="display: flex; justify-content: center; align-items: center; padding: 10px 0;">
            <img src="{logo_url}" alt="Parchem Logo" style="width: 100px;">
        </div>
        """,
        unsafe_allow_html=True
    )
