import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class EncryptionUtility:
    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, plain_text):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plain_text.encode(), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return iv, ct

    def decrypt(self, iv, cipher_text):
        iv = base64.b64decode(iv)
        ct = base64.b64decode(cipher_text)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode('utf-8')

# Example usage:
# key = 'your_secret_key'
# util = EncryptionUtility(key)
# iv, encrypted = util.encrypt('your_message')
# decrypted = util.decrypt(iv, encrypted)