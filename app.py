import streamlit as st
from parchem.auth.firebase import initialize_firebase
from parchem.auth.components import show_login, show_signup, display_logo, show_login_prompt
from parchem.auth.service import check_session, logout, get_current_user, save_message_to_firestore
from parchem.llm.chains import initialize_chain
from parchem.email.handler import configure_email_settings, send_order_email
from parchem.orders.processor import handle_order_step
from parchem.ui.components import initialize_session_state, display_chat_history
from parchem.config import ORDER_FIELDS

st.set_page_config(page_title="parchem_ai", page_icon="https://www.parchem.com/images/logo.svg" )
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
        login_clicked = show_login()

    with tab2:
        signup_clicked = show_signup()

    # Rerun only if a successful login or signup occurred
    if login_clicked or signup_clicked:
        st.rerun()

    st.stop()

# Logout button
if st.sidebar.button("Logout"):
    logout()
    st.session_state.clear()  # Clear the entire session state
    st.rerun()

# Display user info
current_user = get_current_user()
user_id = current_user['localId'] if current_user else None
if current_user:
    st.sidebar.success(f"Logged in as: {current_user['email']}")

# Display success messages if they exist
if 'signup_success' in st.session_state:
    st.success(st.session_state.signup_success)
    del st.session_state.signup_success

if 'login_success' in st.session_state:
    st.success(st.session_state.login_success)
    del st.session_state.login_success

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
        # Save user message to session state
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Get current user ID
        user_id = current_user['localId'] if current_user else None

        # Generate response
        chain = st.session_state.chain
        response = chain.run(input=prompt)
        response = response.replace("### ", "#### ")

        # Save assistant response to session state
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Save both user query & assistant response together in Firestore
        if user_id:
            save_message_to_firestore(user_id, prompt, response)

        # Check for order initiation
        if "Please enter the required details" in response:
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
        # Save entire order details as user query in Firestore
        if user_id:
            order_details = st.session_state.current_order
            order_query = f"Order details: {order_details}"
            save_message_to_firestore(user_id, order_query, "Order received! Our team will contact you shortly.")
        
        # Send email after order completion
        if send_order_email(st.session_state.current_order):
            st.session_state.messages.append({
                "role": "assistant",
                "content": "Order received! Our team will contact you shortly."
            })

        # Reset order mode and order details
        st.session_state.order_mode = False
        st.session_state.current_order = {}
        st.rerun()