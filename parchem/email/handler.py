# Email handling
import smtplib
import streamlit as st
from .templates import create_order_email
from parchem.config import SMTP_SERVER, SMTP_PORT, DEFAULT_RECIPIENT

def configure_email_settings():
    """Securely configure email credentials"""
    if 'email_configured' not in st.session_state:
        if 'CHEM_APP_EMAIL' in st.secrets and 'CHEM_APP_PASSWORD' in st.secrets:
            st.session_state.email = st.secrets["CHEM_APP_EMAIL"]
            st.session_state.password = st.secrets["CHEM_APP_PASSWORD"]
        else:
            with st.sidebar:
                st.header("Email Configuration")
                st.session_state.email = st.text_input("Email address")
                st.session_state.password = st.text_input("App password", type="password")
                if st.button("Save Configuration"):
                    st.success("Configuration saved!")
        st.session_state.email_configured = True

def send_order_email(order_details: dict) -> bool:
    """Send order email with error handling"""
    try:
        msg = create_order_email(st.session_state.email, "naveed49478@gmail.com", order_details)
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(st.session_state.email, st.session_state.password)
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email Error: {str(e)}")
        return False
