import streamlit as st
import pyrebase

def initialize_firebase():
    """
    Initialize Firebase using Pyrebase with JSON configuration.
    """
    if 'firebase' not in st.session_state:
        try:
            # Load Firebase configuration from your JSON file
            firebase_config = {
                "apiKey": st.secrets["FIREBASE"]["apiKey"],
                "authDomain": st.secrets["FIREBASE"]["authDomain"],
                "projectId": st.secrets["FIREBASE"]["projectId"],
                "databaseURL": st.secrets["FIREBASE"]["databaseURL"],
                "storageBucket": st.secrets["FIREBASE"]["storageBucket"],
                "messagingSenderId": st.secrets["FIREBASE"]["messagingSenderId"],
                "appId": st.secrets["FIREBASE"]["appId"],
                "serviceAccount": "parchem/parchem-app-03d4cab1485c.json"  # Replace with the correct path
            }

            # Initialize Pyrebase instance
            st.session_state.firebase = pyrebase.initialize_app(firebase_config)
            st.session_state.auth = st.session_state.firebase.auth()
            #st.success("Firebase initialized successfully!")
        except Exception as e:
            st.error(f"Failed to initialize Firebase: {str(e)}")
            st.stop()
