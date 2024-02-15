import mysql.connector
import pymysql

def create_database_and_tables():
    # Connect to MySQL server

    timeout = 10
    connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
   # db="qr_code_db",
    host="mysql-3fe1618-ravi.a.aivencloud.com",
    password="AVNS_nGLwBVND43BxPGrKzp7",
    read_timeout=timeout,
    port=26950,
    user="avnadmin",
    write_timeout=timeout,
    )
  

    cursor = connection.cursor()

    try:
        # Create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS qr_code_db")
        print("Database created successfully")

        # Use the database
        cursor.execute("USE qr_code_db")

        # Create qr_codes table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS qr_codes (
                qr_code_id INT PRIMARY KEY,
                qr_code_image_url VARCHAR(255),
                qr_code_url VARCHAR(255) UNIQUE,
                INDEX (qr_code_url)
            )
        """)
        print("qr_codes table created successfully")
        cursor.execute("""
            INSERT INTO qr_codes (qr_code_id,qr_code_image_url, qr_code_url) 
            VALUES 
            (12345, 'image/001.png', 'bit.ly/3Eja2q5'),
            (67890, 'image/002.png', 'tinyurl.com/y4zus8kr'),
            (54321, 'image/003.png', 'is.gd/7TgAg9'),
            (98765, 'image/004.png', 'goo.gl/JZRVKu'),
            (24680, 'image/005.png', 'ow.ly/ijZa30rVukC'),
            (13579, 'image/006.png', 'rb.gy/ia2fnj'),
            (86420, 'image/007.png', 't.co/VwRt24QkCU'),
            (97531, 'image/008.png', 'buff.ly/3GHkxVW'),
            (80246, 'image/009.png', 'qr.ae/pGKXqB'),
            (19283, 'image/010.png', 'cutt.ly/VXZSpdP'),
            (47561, 'image/011.png', 'adf.ly/1ZB7tX'),
            (62438, 'image/012.png', 'u.nu/gjf7'),
            (93657, 'image/013.png', 'qrco.de/bVuEj'),
            (31042, 'image/014.png', 'shrinke.me/8NLZ'),
            (50762, 'image/015.png', 'qr.net/FZDZ'),
            (85914, 'image/016.png', 'qlnk.io/qlnk/jahsjd'),
            (72648, 'image/017.png', 'tiny.cc/c5n1tz'),
            (29754, 'image/018.png', 'shrtco.de/BC1DF'),
            (63829, 'image/019.png', 'qrco.de/bV'),
            (38574, 'image/020.png', 'qr.net/FZ'),
            (16294, 'image/021.png', 'bit.ly/3Eja2q6'),
            (73928, 'image/022.png', 'tinyurl.com/y4zus8ks'),
            (47612, 'image/023.png', 'is.gd/7TgAg8'),
            (83916, 'image/024.png', 'goo.gl/JZRVKv'),
            (29584, 'image/025.png', 'ow.ly/ijZa30rVukD'),
            (73849, 'image/026.png', 'rb.gy/ia2fnk'),
            (30519, 'image/027.png', 't.co/VwRt24QkCV'),
            (57139, 'image/028.png', 'buff.ly/3GHkxVX'),
            (18204, 'image/029.png', 'qr.ae/pGKXqA'),
            (84926, 'image/030.png', 'cutt.ly/VXZSpdQ'),
            (26483, 'image/031.png', 'adf.ly/1ZB7tY'),
            (74829, 'image/032.png', 'u.nu/gjf8'),
            (91573, 'image/033.png', 'qrco.de/bVuEk'),
            (57293, 'image/034.png', 'shrinke.me/8NLX'),
            (42839, 'image/035.png', 'qr.net/FZDX'),
            (93857, 'image/036.png', 'qlnk.io/qlnk/jahsjc'),
            (37591, 'image/037.png', 'tiny.cc/c5n1ty'),
            (29486, 'image/038.png', 'shrtco.de/BC1DE'),
            (49582, 'image/039.png', 'qrco.de/bVuEi'),
            (61739, 'image/040.png', 'qr.net/FZDY'),
            (58294, 'image/041.png', 'bit.ly/3Eja2q7'),
            (20495, 'image/042.png', 'tinyurl.com/y4zus8kt'),
            (72935, 'image/043.png', 'is.gd/7TgAg7'),
            (36572, 'image/044.png', 'goo.gl/JZRVKw'),
            (90182, 'image/045.png', 'ow.ly/ijZa30rVukE'),
            (57392, 'image/046.png', 'rb.gy/ia2fnl'),
            (20395, 'image/047.png', 't.co/VwRt24QkCW'),
            (64829, 'image/048.png', 'buff.ly/3GHkxVV'),
            (10573, 'image/049.png', 'qr.ae/pGKXqZ'),
            (89274, 'image/050.jpg', '3qq.com/001')


        """)
        # Create keys table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS qr_keys (
                id INT AUTO_INCREMENT PRIMARY KEY,
                qr_code_id INT,
                qr_code_url VARCHAR(255),
                `key` VARCHAR(255) UNIQUE,
                FOREIGN KEY (qr_code_url) REFERENCES qr_codes(qr_code_url)
            )
        """)


        print("keys table created successfully")

        # Create user_data table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_data (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                qr_code_id INT,
                password VARCHAR(255),
                email VARCHAR(100),
                name  VARCHAR(36),
                gender TEXT,
                age INT,
                FOREIGN KEY (qr_code_id) REFERENCES qr_codes(qr_code_id)
            )
        """)
        print("user_data table created successfully")

    except mysql.connector.Error as error:
        print("Error:", error)

    finally:
        # Close cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
    create_database_and_tables()
