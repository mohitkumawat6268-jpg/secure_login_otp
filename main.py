from database import connect
from auth import register, login
from otp import generate_otp, verify_otp

connect()

while True:
    print("\n==== SECURE LOGIN SYSTEM ====")
    print("1. Register")
    print("2. Login with OTP")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        register(username, password)

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        if login(username, password):

            otp = generate_otp()
            print(f"\n🔐 Your OTP is: {otp}")

            user_otp = input("Enter OTP: ")

            if verify_otp(otp, user_otp):
                print("✅ Login successful (OTP verified)")
            else:
                print("❌ Invalid OTP")

    elif choice == "3":
        break

    else:
        print("Invalid option")