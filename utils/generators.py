import random
import secrets
import string


def generate_pub_key(selection_list: list):
    while True:
        code = secrets.token_urlsafe(5)
        if code not in selection_list:
            break
        continue
    return code


def generate_pri_key(public_key: str):

    code = random.choices(string.ascii_lowercase, k=5)
    return public_key + "".join(code)
