# app.py
import streamlit as st
from parchem.auth.firebase import initialize_firebase
from parchem.auth.components import show_login, show_signup, display_logo,show_login_prompt  # Import the display_logo function
from parchem.auth.service import check_session, logout, get_current_user
from parchem.llm.chains import initialize_chain
from parchem.email.handler import configure_email_settings, send_order_email
from parchem.orders.processor import handle_order_step
from parchem.ui.components import initialize_session_state, display_chat_history
from parchem.config import ORDER_FIELDS

# Set page configuration
def load_css():
    with open('parchem/assets/styles.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Call the load_css function
load_css()

# Display the Parchem logo in the sidebar
display_logo()

# Initialize Firebase
initialize_firebase()

# Authentication Check
if not check_session():
    show_login_prompt()
    tab1, tab2 = st.sidebar.tabs(["Login", "Sign Up"])

    with tab1:
        show_login()

    with tab2:
        show_signup()

    st.stop()

# Logout button
if st.sidebar.button("Logout"):
    logout()

# Display user info
current_user = get_current_user()
if current_user:
    st.sidebar.success(f"Logged in as: {current_user['email']}")

# Initialize user-specific chain
if 'chain' not in st.session_state:
    st.session_state.chain = initialize_chain()

# Initialize session state variables
initialize_session_state()

# Display chat history
display_chat_history()

# Configure email settings
configure_email_settings()

# Chatbot logic
if not st.session_state.order_mode:
    if prompt := st.chat_input("Ask about chemicals..."):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Get chain from session state
        chain = st.session_state.chain
        
        # Generate response with memory
        response = chain.run(input=prompt)
        
        # Add assistant response
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Check for order initiation
        if "Please enter the required details in the chat box to proceed with your order." in response:
            st.session_state.order_mode = True
            st.session_state.current_order = {}

        st.rerun()

# Order processing logic
if st.session_state.order_mode:
    for field, prompt in ORDER_FIELDS.items():
        handle_order_step(field, prompt)
        if field not in st.session_state.current_order:
            break
    else:
        if send_order_email(st.session_state.current_order):
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Order received! Our team will contact you shortly."
            })
        st.session_state.order_mode = False
        st.session_state.current_order = {}
        st.rerun()
