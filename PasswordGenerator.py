import random
import string

RANDOM_PWD_LEN = 20
RANDOM_PWD_CHARS = string.ascii_letters + \
                   string.digits + \
                   string.punctuation


def generate_password() -> str:
    pwd = "".join([random.choice(RANDOM_PWD_CHARS) for _ in range(RANDOM_PWD_LEN)])
    return pwd
