# code orders/processor.py is below  
import datetime
import streamlit as st
from parchem.config import   UNIT_OPTIONS
def validate_email(email: str) -> bool:
    """Simple email validation checking for '@' and domain structure."""
    return '@' in email and '.' in email.split('@')[-1]

def handle_order_step(field: str, prompt: str):
    """Handle different input types for order collection"""
    if field not in st.session_state.current_order:
        # if field == 'packaging':
        #     selection = st.selectbox(prompt, PACKAGING_OPTIONS)
        #     if st.button("Submit"):
        #         st.session_state.current_order[field] = selection
        #         st.session_state.messages.append({"role": "user", "content": selection})
        #         st.rerun()
        #elif field == 'unit':
        if field == 'unit':
            selection = st.selectbox(prompt, UNIT_OPTIONS)
            if st.button("Submit"):
                st.session_state.current_order[field] = selection
                st.session_state.messages.append({"role": "user", "content": selection})
                st.rerun()
        elif field == 'delivery_date':
            date = st.date_input(prompt, min_value=datetime.date.today())
            if st.button("Submit"):
                formatted_date = date.strftime("%m/%d/%Y")
                st.session_state.current_order[field] = formatted_date
                st.session_state.messages.append({"role": "user", "content": formatted_date})
                st.rerun()
        else:
            response = st.chat_input(prompt)
            if response:
                # Always add user's raw input to chat history first
                st.session_state.messages.append({"role": "user", "content": response})
                valid = True
                error_message = ""
                processed_value = response

                # Field-specific validation
                if field == 'email':
                    if not validate_email(response):
                        error_message = "Please enter a valid email address (e.g., user@example.com)."
                        valid = False
                elif field == 'quantity':
                    try:
                        processed_value = int(response)
                        if processed_value <= 0:
                            raise ValueError
                    except ValueError:
                        error_message = "Please enter a positive whole number for quantity."
                        valid = False

                # Handle validation result
                if not valid:
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    st.rerun()
                else:
                    st.session_state.current_order[field] = processed_value
                    st.rerun()
        # else:
        #     response = st.chat_input(prompt)
        #     if response:
        #         st.session_state.current_order[field] = response
        #         st.session_state.messages.append({"role": "user", "content": response})
        #         st.rerun()