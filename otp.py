import random


def generate_otp():
    return str(random.randint(100000, 999999))


def verify_otp(generated_otp, user_input):
    return generated_otp == user_input