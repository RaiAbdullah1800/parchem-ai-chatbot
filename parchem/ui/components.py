# UI components
import streamlit as st

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "order_mode" not in st.session_state:
        st.session_state.order_mode = False
    if "current_order" not in st.session_state:
        st.session_state.current_order = {}

def display_chat_history():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])