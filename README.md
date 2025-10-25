
# 🔐 QR Code Authentication and Data Entry

This project provides a **Streamlit web application** for **QR code-based authentication** and **secure user data entry** with **admin control**.  
It uses **OpenCV**, **pyzbar**, and **MySQL** for scanning, decoding, and storing data, making it ideal for secure registrations or controlled access systems.

---

## 🧩 Features

- 📷 **Scan QR codes** using camera or image upload  
- 🔑 **Verify QR code keys** with MySQL backend  
- 👤 **User registration** (passwords securely hashed using SHA-256)  
- 🧾 **Admin panel** to:
  - Add QR code details  
  - Delete user entries  
  - View database tables  
- 💾 **Persistent MySQL integration** for data storage  
- 🖼️ **Live video preview** during QR code scanning  

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **Streamlit** (web app)
- **OpenCV** (`cv2`)
- **pyzbar** (QR decoding)
- **Pillow (PIL)** (image handling)
- **pymysql** (database connectivity)
- **pandas** (table visualization)
- **hashlib** (password hashing)

---

## 🏗️ Installation

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd qr-auth-app
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---


---

## 🚀 Run the App

```bash
streamlit run app.py
```

Then open the provided local URL (usually [http://localhost:8501](http://localhost:8501)) in your browser.

---

## 🗃️ Database Setup

This app connects to a **MySQL** database with three main tables:

### 1. `qr_codes`

| Column            | Type     | Description       |
| ----------------- | -------- | ----------------- |
| qr_code_id        | INT (PK) | Unique QR ID      |
| qr_code_image_url | VARCHAR  | Image URL         |
| qr_code_url       | VARCHAR  | URL encoded in QR |

### 2. `qr_keys`

| Column      | Type     | Description              |
| ----------- | -------- | ------------------------ |
| qr_code_id  | INT (FK) | Links to `qr_codes`      |
| qr_code_url | VARCHAR  | URL from QR              |
| key         | VARCHAR  | Secret key input by user |

### 3. `user_data`

| Column     | Type     | Description             |
| ---------- | -------- | ----------------------- |
| qr_code_id | INT (FK) | Linked QR ID            |
| password   | VARCHAR  | SHA-256 hashed password |
| email      | VARCHAR  | User email              |
| name       | VARCHAR  | User name               |
| gender     | VARCHAR  | User gender             |
| age        | INT      | User age                |

---

## 🔑 Admin Credentials (Default)

```
Username: admin  
Password: admin
```

---

## 🧭 How It Works

1. **User Mode**

   * Upload or scan a QR code.
   * Enter a unique key to verify.
   * Register personal details once verified.

2. **Admin Mode**

   * Add or manage QR code records.
   * Delete user data and associated keys.
   * View all stored records in tabular format.

---

## ⚠️ Notes

* Make sure your **MySQL credentials** in the script are correct.
* Update the `host`, `user`, `password`, and `db` fields in the code as needed.
* The camera path `/dev/video*` may vary — adjust if required.
* Ensure `bg.jpeg` exists in the working directory.

---

```

---

Would you like me to also generate a **`requirements.txt`** file you can directly download for this project?
```
