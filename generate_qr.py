import pyotp
import qrcode
import sys

# Reference: https://pyauth.github.io/pyotp/

def generate_qr():
    # helper function to generate a 32-character base32 secret
    # compatible with Google Authenticator and other OTP apps.
    secret = pyotp.random_base32()
    
    with open('secret.txt', 'w') as f:
        f.write(secret)
    
    totp = pyotp.TOTP(secret)

    # Secret keys may be encoded in QR codes as a URI with the following format:
    # otpauth://TYPE/LABEL?PARAMETERS
    # Example: otpauth://totp/Example:alice@google.com?secret=JBSWY3DPEHPK3PXP&issuer=Example
    uri = totp.provisioning_uri(name="user@example.com", issuer_name="ExampleApp")
    
    qr = qrcode.make(uri)
    qr.save("otp_qr.jpg")
    
    print("QR code generated and saved as otp_qr.jpg")

if __name__ == "__main__":
    generate_qr()

