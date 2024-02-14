import mysql.connector
import pymysql

# Function to delete the database
def delete_database():
    try:
        # Connect to MySQL server
    
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
