import streamlit as st
import mysql.connector
import hashlib
import os
import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import pandas as pd
import pymysql

st.title('QR Code Authentication and Data Entry')
st.image('bg.jpeg')

option = st.sidebar.radio("Select Option", ('User', 'Admin'))
frameplaceholder=st.empty()

# Function to check if key exists for QR code
def check_key_exists(qr_code_id, entered_key, cursor):
    query = "SELECT * FROM qr_keys WHERE qr_code_id = %s or `key` = %s"
    cursor.execute(query, (qr_code_id, entered_key))
    result = cursor.fetchone()
    return result is not None

# Function to store user data
def store_user_data(qr_code_id, password, email, name, gender, age, cursor):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    query = "INSERT INTO user_data (qr_code_id, password, email, name, gender, age) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (qr_code_id, hashed_password, email, name, gender, age))

# Function to scan QR code using CV2
def scan_qr_code():
    qr_code_id = None
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        cv2.imshow("QR Code Scanner", frame)
        frameplaceholder.image(frame,channels='BGR')
        decoded_objects = decode(frame)
        if decoded_objects:
            qr_code_id = decoded_objects[0].data.decode('utf-8')
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return qr_code_id

# Streamlit app layout
def main():

    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host="mysql-3fe1618-ravi.a.aivencloud.com",
    password="AVNS_nGLwBVND43BxPGrKzp7",
    read_timeout=timeout,
    port=26950,
    user="avnadmin",
    write_timeout=timeout,
    )

    cursor = connection.cursor()

    qr_code_id = None  # Initialize qr_code_id outside the conditional blocks

    if option == 'Admin':
        # Admin Login
        admin_username = st.text_input("Admin Username")
        admin_password = st.text_input("Admin Password", type="password")
        if admin_username == "admin" and admin_password == "admin":
            st.success("Logged in as admin")
            operation = st.radio("Select Operation", ('Add QR Code', 'Delete Entry', 'Display Tables'))

            if operation == 'Add QR Code':
                qr_id = st.text_input("Enter QR ID:")
                qr_code_img_url = st.text_input("Enter QR Code Image URL:")
                qr_url = st.text_input("Enter QR URL:")
                if st.button("Add"):
                    query = "INSERT INTO qr_codes (qr_code_id, qr_code_image_url, qr_code_url) VALUES (%s, %s, %s)"
                    cursor.execute(query, (qr_id, qr_code_img_url, qr_url))
                    st.success("QR Code details added successfully.")

            elif operation == 'Delete Entry':
                user_names_query = "SELECT qr_code_id, name FROM user_data"
                cursor.execute(user_names_query)
                user_names = cursor.fetchall()
                user_id = st.selectbox("Select User to Delete:", [f"{name} (ID: {id})" for id, name in user_names])
                if st.button("Delete"):
                    selected_user_id = int(user_id.split("ID: ")[-1][:-1])
                    # Deleting user data
                    delete_user_query = "DELETE FROM user_data WHERE qr_code_id = %s"
                    cursor.execute(delete_user_query, (selected_user_id,))
                    # Deleting related qr_keys
                    delete_qr_keys_query = "DELETE FROM qr_keys WHERE qr_code_id = %s"
                    cursor.execute(delete_qr_keys_query, (selected_user_id,))
                    st.success("User data and related QR Keys deleted successfully.")

            elif operation == 'Display Tables':
                tables = st.multiselect("Select Tables to Display:", ['qr_codes', 'qr_keys', 'user_data'])
                if tables:
                    for table_name in tables:
                        st.write(f"### {table_name} Table")
                        cursor.execute(f"SELECT * FROM {table_name}")
                        data = cursor.fetchall()
                        if data:
                            df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])
                            st.dataframe(df)
                        else:
                            st.write("Table is empty.")

    else:
        # User Authentication

        if 'verified' not in st.session_state:
            st.session_state.verified = False

        if 'qr_code_url' not in st.session_state:
            st.session_state.qr_code_url = None
        
        if 'qr_code_id' not in st.session_state:
            st.session_state.qr_code_id = None



        if not st.session_state.verified:
            st.write("Select the option to scan QR code:")
            scan_option = st.radio("Scan Option", ('Upload Image', 'Use Camera'))

            if scan_option == 'Upload Image':
                qr_code_image = st.file_uploader("Upload QR Code Image", type=["png", "jpg", "jpeg"])
                if qr_code_image is not None:
                    decoded_objects = decode(Image.open(qr_code_image))
                    if decoded_objects:
                        qr_code_url = decoded_objects[0].data.decode('utf-8')
                        st.write('QR code url:', qr_code_url)
                        st.session_state.qr_code_url = qr_code_url
                        st.session_state.verified = True
            else:  # Use Camera
                qr_code_url = scan_qr_code()  # Assign value to qr_code_id
                if qr_code_url:
                    st.session_state.qr_code_url=qr_code_url
                    st.write('QR code url:', st.session_state.qr_code_url)
                    st.write(qr_code_url)
                    # Fetch ID from database based on the ID obtained from the QR code
                    cursor.execute("SELECT qr_code_id FROM qr_codes WHERE qr_code_url = %s", (qr_code_url,))
                    result = cursor.fetchone()
                    st.write(result)
                    if result:
                        qr_code_id = result[0]
                        st.session_state.qr_code_id=qr_code_id
                        st.write('QR code id: ',st.session_state.qr_code_id)
                    st.session_state.verified = True


        if st.session_state.verified:
            # Enter manual key
            entered_key = st.text_input("Enter the key for the QR code:")

            # Check if key exists for QR code
            if st.button("Verify Key"):
                st.write(st.session_state.qr_code_id)
                if st.session_state.qr_code_id is None:
                    st.error("Error: QR code ID not found.")
                elif check_key_exists(st.session_state.qr_code_id, entered_key, cursor):
                    st.error("Error: The key entered is not valid for this QR code. Please try again.")
                else:
                    st.session_state.verified = True
                    add_key_query = "INSERT INTO qr_keys (qr_code_id,qr_code_url, `key`) VALUES (%s, %s,%s)"
                    cursor.execute(add_key_query, (st.session_state.qr_code_id,st.session_state.qr_code_url, entered_key))
                    st.success("Key added to the table.")
                    st.success("Key verified. Please enter your details.")

        if st.session_state.verified:

            password = st.text_input("Enter your password:")
            email = st.text_input("Enter your email:")
            name = st.text_input("Enter your name:")
            gender = st.text_input("Select your gender:")
            age = st.text_input("Enter your age:")

            # Store user data
            if st.button("Submit") and password and email and name and gender and age:
                store_user_data(st.session_state.qr_code_id, password, email, name, gender, age, cursor)
                st.success("User data stored successfully.")

    # Commit changes and close cursor and connection
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
