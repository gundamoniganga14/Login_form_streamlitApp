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
def register_user(name, email, password):
    conn = mysql.connector.connect(
        host="localhost",
        