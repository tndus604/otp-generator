import pyotp
import qrcode
import sys
import time

# Reference: https://pyauth.github.io/pyotp/

def generate_qr():
    # Helper function to generate a 32-character base32 secret
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
    
    print("QR code generated and saved as `otp_qr.jpg`")

def get_otp():
    with open('secret.txt', 'r') as f:
        secret = f.read().strip()
    
    totp = pyotp.TOTP(secret)
    
    while True:
        print("Current OTP:", totp.now())

        # Countdown 30 seconds
        for remaining in range(30, 0, -1):
            print(f"Next OTP in {remaining} seconds", end='\r')
            time.sleep(1)
        
        # Removes the countdown line after retrieving a new OTP
        print(' ' * 30, end='\r')

def main():
    if len(sys.argv) != 2:
        print("Usage: ./submission --generate-qr or ./submission --get-otp")
        sys.exit(1)

    command = sys.argv[1]

    if command == '--generate-qr':
        generate_qr()
    elif command == '--get-otp':
        get_otp()
    else:
        print("Unknown command")
        sys.exit(1)

if __name__ == "__main__":
    main()
