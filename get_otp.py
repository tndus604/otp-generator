import pyotp
import time

def get_otp():
    with open('secret.txt', 'r') as f:
        secret = f.read().strip()
    
    totp = pyotp.TOTP(secret)
    
    while True:
        print("Current OTP:", totp.now())
        time.sleep(30)
        print(time.sleep(30))

if __name__ == "__main__":
    get_otp()
