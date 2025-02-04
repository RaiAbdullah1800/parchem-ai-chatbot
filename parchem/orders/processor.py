# code orders/processor.py is below  
import datetime
import streamlit as st
# from parchem.config import ORDER_FIELDS, PACKAGING_OPTIONS, UNIT_OPTIONS
from parchem.config import   UNIT_OPTIONS

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
                st.session_state.current_order[field] = response
                st.session_state.messages.append({"role": "user", "content": response})
                st.rerun()