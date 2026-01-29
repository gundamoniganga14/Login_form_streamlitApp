import streamlit as st
import mysql.connector
with st.form("login_form"):
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    login_submitted = st.form_submit_button("Login")
    if login_submitted:
        st.write(f"Login successful! Welcome, {username}.")