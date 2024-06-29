import random
import string

def generate_secret_key(length=50):
    chars = string.ascii_letters + string.digits + "!@#$%^&*(-_=+)"
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))