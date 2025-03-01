import streamlit as st
from datetime import datetime

def save_message_to_firestore(user_id: str, user_query: str, assistant_response: str):
    """
    Save both the user query and assistant response in a single document under the 'messages' collection.
    """
    try:
        message_data = {
            "message": {
                "user_query": user_query,
                "assistant_response": assistant_response
            },
            "timestamp": datetime.now()  # Timestamp for sorting
        }
        # Store in Firestore under users/{userId}/messages/{auto_id}
        st.session_state.db.collection("users").document(user_id).collection("messages").add(message_data)
        return True
    except Exception as e:
        st.error(f"Error saving message: {str(e)}")
        return False


def get_user_messages(user_id: str):
    """
    Retrieve user's chat history sorted by timestamp.
    """
    try:
        messages_ref = (
            st.session_state.db.collection("users")
            .document(user_id)
            .collection("messages")
            .order_by("timestamp")
            .get()
        )
        return [doc.to_dict() for doc in messages_ref]
    except Exception as e:
        st.error(f"Error retrieving messages: {str(e)}")
        return []

def create_user(email: str, password: str):
    """
    Create a new user with email/password using Pyrebase authentication.
    """
    try:
        user = st.session_state.auth.create_user_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        error = eval(e.args[1])['error']['message']
        if error == "EMAIL_EXISTS":
            return None, "Email already exists. Please log in or use a different email."
        elif error == "WEAK_PASSWORD":
            return None, "Password should be at least 6 characters."
        return None, f"Signup error: {error}"

def authenticate_user(email: str, password: str):
    """
    Authenticate a user with email/password using Pyrebase authentication.
    """
    try:
        user = st.session_state.auth.sign_in_with_email_and_password(email, password)
        return user, None
    except Exception as e:
        error = eval(e.args[1])['error']['message']
        if error == "INVALID_PASSWORD" or error == "EMAIL_NOT_FOUND":
            return None, "Invalid email or password."
        return None, f"Login error: {error}"

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
