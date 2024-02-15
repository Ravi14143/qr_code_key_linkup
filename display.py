import mysql.connector
import pymysql

# Function to fetch and display data from qr_codes table
def display_qr_code_data(cursor):
    try:
        # Fetch data from qr_codes table
        cursor.execute("show databases")
        qr_codes_data = cursor.fetchall()

        print(qr_codes_data)

        cursor.execute("select * from qr_codes")
        qr_codes_data = cursor.fetchall()

        print(qr_codes_data)

        cursor.execute("select * from qr_keys")
        qr_codes_data = cursor.fetchall()
        print(qr_codes_data)

        cursor.execute("select * from user_data")
        qr_codes_data = cursor.fetchall()
        print(qr_codes_data)

    except mysql.connector.Error as error:
        print("Error:", error)

# Main function
def main():
    # Connect to MySQL database
    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="qr_code_db",
    host="mysql-3fe1618-ravi.a.aivencloud.com",
    password="AVNS_nGLwBVND43BxPGrKzp7",
    read_timeout=timeout,
    port=26950,
    user="avnadmin",
    write_timeout=timeout,
    )
  
    cursor = connection.cursor()

    try:
        # Display data from qr_codes table
        display_qr_code_data(cursor)
    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    main()
