import mysql.connector

# Function to fetch and display data from qr_codes table
def display_qr_code_data(cursor):
    try:
        # Fetch data from qr_codes table
        cursor.execute("SELECT * FROM qr_codes")
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
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mrk*14143",
        database="qr_code_db"
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
