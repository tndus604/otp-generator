# OTP Generator

## Description
This project is a application that generates and retrieves one-time passwords (OTPs) using the TOTP (Time-based One-Time Password) algorithm. It includes functionality to generate a QR code for setting up the OTP in an authenticator app and to continuously display the current OTP.

## Implementation
The implementation consists of the following components:
- **`main.py`**: The main script that contains two main functionalities:
  - `generate_qr()`: Generates a QR code for the OTP and saves it as `otp_qr.jpg`. The corresponding secret is saved in `secret.txt`.
  - `get_otp()`: Continuously displays the current OTP in 30-second intervals.
- **`Makefile`**: Automates the build and run processes for the application.

## Requirements
- Python3
- `pyotp` library
- `qrcode` library

You can install the required libraries using:
```sh
pip install pyotp qrcode
```

## Usage
1. The Makefile includes targets to simplify running the commands. In your terminal, type:
    ```
    make
    ```

2. To generate a QR code for setting up the OTP in an authenticator app, run:
    ```
    ./submission --generate-qr
    ```

3. To display the current OTP, run:
    ```
    ./submission --get-otp
    ```

## Example Output
- **QR Code:**
    ![example_qrcode](./assets/otp_qr_example.jpg)

- **Terminal Output:**
    ![get_otp](./assets/get_otp_terminal.png)


