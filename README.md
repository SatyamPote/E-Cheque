# E-Cheque System

## Overview

This project implements a basic e-cheque system using Django, Python, and cryptographic signatures. It allows users to issue e-cheques, view a blockchain of issued cheques, and verify the validity of cheques.  The system utilizes RSA encryption for signing and verification.

## Features

*   **Issue E-Cheques:** Create new cheques with payee name, amount, and date.
*   **Blockchain:** View a simple blockchain containing all issued cheques.
*   **Verification:** Verify the authenticity of a cheque using its signature.
*   **Admin Interface:** Manage cheques and blocks through the Django admin panel.

## Technologies Used

*   **Python:** The primary programming language.
*   **Django:** A high-level Python web framework.
*   **pycryptodome:** A cryptographic library for RSA encryption and signing.
*   **SQLite:** A lightweight database for storing cheque and blockchain data (default).

## Getting Started

### Prerequisites

*   **Python 3.12 or higher:**  Ensure you have Python installed on your system.
*   **pip:** Python package installer.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository URL]
    cd echeque_project
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    (Create a `requirements.txt` file with the following content):

    ```
    Django
    pycryptodome
    ```

### Key Generation

Before running the application, you need to generate RSA key pairs for signing and verification.

1.  **Navigate to the `keys` directory:**

    ```bash
    cd keys
    ```

2.  **Run the key generation script:**

    ```bash
    python generate_keys.py
    ```

    This will create `private.pem` and `public.pem` files in the `keys` directory. **Keep the `private.pem` file secure!**

### Database Setup

1.  **Make migrations:**

    ```bash
    python manage.py makemigrations cheques
    ```

2.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

### Running the Application

1.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

2.  **Access the application in your browser:**

    *   **Admin Interface:** `http://127.0.0.1:8000/admin/` (Create a superuser if prompted: `python manage.py createsuperuser`)
    *   **Home Page:** `http://127.0.0.1:8000/cheques/`

## Usage

1.  **Create a Cheque:**
    *   Navigate to `http://127.0.0.1:8000/cheques/create_cheque/`.
    *   Fill in the payee, amount, and date.
    *   Submit the form.

2.  **View the Blockchain:**
    *   Navigate to `http://127.0.0.1:8000/cheques/blockchain/`.
    *   View the list of issued cheques and their corresponding block hashes.

3.  **Verify a Cheque:**
    *   Navigate to `http://127.0.0.1:8000/cheques/verify_cheque_form/`.
    *   Enter the payee, amount, date, and **signature** of the cheque you want to verify.
    *   **To get the signature:** Go to the admin interface, find the cheque, and copy the value of the "Signature" field.
    *   Submit the form.  The system will indicate whether the cheque is valid or tampered with.

## Project Structure
