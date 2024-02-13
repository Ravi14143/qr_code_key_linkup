import mysql.connector

# Function to delete the database
def delete_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mrk*14143"
        )
        cursor = connection.cursor()

        # Drop the database
        cursor.execute("DROP DATABASE IF EXISTS qr_code_db")
        print("Database deleted successfully")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    delete_database()
