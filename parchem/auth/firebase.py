import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

def initialize_firebase():
    """
    Initialize Firebase Admin SDK for Firestore and Pyrebase for Authentication.
    """
    if 'firebase_initialized' not in st.session_state:
        try:
            # Load Firebase service account JSON from Streamlit secrets
            firebase_service_account_json = st.secrets["FIREBASE_SERVICE_ACCOUNT_JSON"]["json"]
            firebase_config = json.loads(firebase_service_account_json)

            # ✅ Initialize Firebase Admin SDK (for Firestore)
            if not firebase_admin._apps:
                cred = credentials.Certificate(firebase_config)
                firebase_admin.initialize_app(cred)

            # ✅ Initialize Firestore Client
            st.session_state.db = firestore.client()

            # ✅ Initialize Pyrebase (for Authentication)
            pyrebase_config = {
                "apiKey": st.secrets["FIREBASE"]["apiKey"],
                "authDomain": st.secrets["FIREBASE"]["authDomain"],
                "projectId": st.secrets["FIREBASE"]["projectId"],
                "databaseURL": st.secrets["FIREBASE"]["databaseURL"],
                "storageBucket": st.secrets["FIREBASE"]["storageBucket"],
                "messagingSenderId": st.secrets["FIREBASE"]["messagingSenderId"],
                "appId": st.secrets["FIREBASE"]["appId"],
                "serviceAccount":firebase_config
            }
            firebase = pyrebase.initialize_app(pyrebase_config)

            # Store Firebase authentication in session state
            st.session_state.auth = firebase.auth()

            # Mark Firebase as initialized
            st.session_state.firebase_initialized = True

        except Exception as e:
            st.error(f"Failed to initialize Firebase: {str(e)}")
            st.stop()
