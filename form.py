import streamlit as st
import mysql.connector
#form
with st.form("my_form"):
    st.title(" Registration form")
    name = st.text_input("Enter your name:")
    password= st.text_input("password:", type="password")
    confirm_password= st.text_input("confirm password:", type="password")
    useremail= st.text_input("email:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("submitted successfully")
        if password==confirm_password:
            st.success("password matched")
            # Create a connection to the MySQL database
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ganga@1407_",
                database="form_db"
            )
            cursor = conn.cursor()
            #create database
            cursor.execute("CREATE DATABASE IF NOT EXISTS form_db")
            cursor.execute("USE form_db")
            cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))")

            # Insert user data into the database
            insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (name, useremail, password)
            cursor.execute(insert_query, values)
            conn.commit()

            st.success("User registered successfully!")

            # Close the database connection
            cursor.close()
            conn.close()
        else:
            st.error("password not matched")

