import streamlit as st

def create_user(email: str, password: str):
    """
    Create a new user with email/password using Pyrebase.
    """
    try:
        user = st.session_state.auth.create_user_with_email_and_password(email, password)
        st.success("Account created successfully!")
        return user
    except Exception as e:
        st.error(f"Signup Error: {str(e)}")
        return None

def authenticate_user(email: str, password: str):
    """
    Authenticate a user with email/password using Pyrebase.
    """
    try:
        user = st.session_state.auth.sign_in_with_email_and_password(email, password)
        st.session_state.user = user
        return user
    except Exception as e:
        st.error(f"Login Error: {str(e)}")
        return None

def check_session():
    """
    Check if a user is logged in.
    """
    return 'user' in st.session_state

def logout():
    """
    Log out the current user.
    """
    if 'user' in st.session_state:
        del st.session_state.user
    st.success("Logged out successfully!")
    st.rerun()

def get_current_user():
    """
    Get the current logged-in user.
    """
    return st.session_state.get('user')
