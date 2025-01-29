import streamlit as st
import pyrebase
import json

def initialize_firebase():
    """
    Initialize Firebase using Pyrebase with JSON configuration from Streamlit secrets.
    """
    if 'firebase' not in st.session_state:
        try:
            # Load Firebase service account JSON from Streamlit secrets
            firebase_service_account_json = st.secrets["FIREBASE_SERVICE_ACCOUNT_JSON"]["json"]

            # Parse the JSON string to a dictionary
            firebase_config = json.loads(firebase_service_account_json)

            # Setup Firebase config from secrets
            firebase_config = {
                "apiKey": st.secrets["FIREBASE"]["apiKey"],
                "authDomain": st.secrets["FIREBASE"]["authDomain"],
                "projectId": st.secrets["FIREBASE"]["projectId"],
                "databaseURL": st.secrets["FIREBASE"]["databaseURL"],
                "storageBucket": st.secrets["FIREBASE"]["storageBucket"],
                "messagingSenderId": st.secrets["FIREBASE"]["messagingSenderId"],
                "appId": st.secrets["FIREBASE"]["appId"],
                "serviceAccount": firebase_config  # Use service account dict from JSON
            }

            # Initialize Pyrebase instance
            st.session_state.firebase = pyrebase.initialize_app(firebase_config)
            st.session_state.auth = st.session_state.firebase.auth()
            
        except Exception as e:
            st.error(f"Failed to initialize Firebase: {str(e)}")
            st.stop()
