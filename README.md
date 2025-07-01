# 💳 E-Cheque System

## 🧾 Overview

This project implements a basic **E-Cheque System** using Django, Python, and cryptographic signatures.  
It allows users to:

- 📝 Issue e-cheques  
- 🔗 View a blockchain of issued cheques  
- ✅ Verify the validity of cheques  

The system utilizes **RSA encryption** for signing and verification.

---

## 🚀 Features

- ✍️ **Issue E-Cheques**  
- 🧱 **Blockchain of Cheques**  
- 🕵️ **Verification System**  
- ⚙️ **Django Admin Interface**

---

## 🛠️ Technologies Used

- Python  
- Django  
- PyCryptodome  
- SQLite  

---

## 📥 Installation

```bash
# Create and activate a virtual environment
python -m venv venv

# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

```txt
# requirements.txt
Django
pycryptodome
```

---

## 🔑 Key Generation

```bash
# Navigate to the keys directory
cd keys

# Run key generation script
python generate_keys.py
```

```txt
# This creates:
# - private.pem (keep this secure)
# - public.pem (used for verifying signatures)
```

---

## 🗃️ Database Setup

```bash
# Run migrations
python manage.py makemigrations cheques
python manage.py migrate
```

---

## 🚦 Running the Application

```bash
# Start development server
python manage.py runserver
```

```txt
# Access URLs:
# Admin Panel: http://127.0.0.1:8000/admin/
# Home Page:   http://127.0.0.1:8000/cheques/
```

```bash
# Create a Django superuser
python manage.py createsuperuser
```

---

## 🧾 Create a Cheque

```txt
1. Go to: http://127.0.0.1:8000/cheques/create_cheque/
2. Fill in:
   - Payee Name
   - Amount
   - Date
3. Submit to generate and sign a cheque.
```

---

## 🔗 View Blockchain

```txt
- Go to: http://127.0.0.1:8000/cheques/blockchain/
- View all cheques and block metadata in the chain.
```

---

## 🔍 Verify a Cheque

```txt
1. Go to: http://127.0.0.1:8000/cheques/verify_cheque_form/
2. Fill in:
   - Payee
   - Amount
   - Date
   - Signature
3. Copy the signature from the Admin Panel if needed.
4. Submit to validate the cheque.
```

---

## 🖼️ Screenshots

![Homepage](https://github.com/user-attachments/assets/6b74914a-8bc1-46ca-9983-94e2b6a0af43)

*Homepage of the E-Cheque System*

---

![Blockchain View](https://github.com/user-attachments/assets/2b1f5647-4ce2-4a7b-97d6-6108c044a921)

*Blockchain listing all issued cheques*

---

![Verification Form](https://github.com/user-attachments/assets/cf08e205-9207-4768-ac75-dad42fb7ef3f)

*Form to verify cheque authenticity*

---

## 📦 Deployment

```bash
# Set up virtual environment
python -m venv venv

# Activate it:
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files (only if DEBUG=False)
python manage.py collectstatic

# Start server
python manage.py runserver
```

---

## 👨‍💼 Author & License

```txt
Created by [Satyam pote]  
Built using Django, Python & Cryptography  
Licensed under the MIT License  
```
