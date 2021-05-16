import zlib

from cryptography.fernet import Fernet


class Text:
    @staticmethod
    def encode_and_compress(data):
        key = Fernet.generate_key()
        fernet = Fernet(key)
        token = fernet.encrypt(bytes(data, "utf-8"))
        return {"token": zlib.compress(token, 6), "key": key}

    @staticmethod
    def decompress_and_decode(token, key):
        fernet = Fernet(key)
        data = fernet.decrypt(zlib.decompress(token))
        return data
