import hashlib
import binascii
from Crypto.Cipher import AES


class AESCiper(object):
    def __init__(self, key, mode=AES.MODE_ECB):
        self._aes = AES.new(self._get_sha1prng_key(key), mode)

    def _get_sha1prng_key(self, key):
        return hashlib.sha1(hashlib.sha1(key.encode()).digest()).digest()[:16]

    def encrypt_to_hex(self, data: str) -> str:
        return binascii.b2a_hex(self._aes.encrypt(self._padding(data).encode())).decode().upper()

    def decrypt_from_hex(self, data: str) -> str:
        return self._unpadding(self._aes.decrypt(binascii.a2b_hex(data)).decode())

    def _padding(self, s: str) -> str:
        ''' padding PKCS5 '''
        pad_num = 16 - len(s.encode()) % 16  # 中文.encode() has different length
        return s + pad_num * chr(pad_num)

    def _unpadding(self, s: str) -> str:
        ''' unpadding PKCS5 '''
        padding_num = ord(s[-1])
        return s[: -padding_num]
