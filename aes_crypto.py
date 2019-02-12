from Crypto import Random
from Crypto.Cipher import AES
import base64


class AESCrypto:
    def __init__(self, key, value_of):
        self.value_of = value_of[-6:]
        self.key = self.generate_key(key)
        self.BLOCK_SIZE = 16

    def generate_key(self, key):
        def change_name(name, index, rate):
            while len(name) - 1 < index:
                index = index - len(name)
            _str = name[:index]
            total = ""
            for iw in range(rate):
                total += name[index]
            _str = _str + total + name[index:]
            return _str

        for i in range(3):
            defined = self.value_of[i * 2:i * 2 + 2]
            defined_index = int(defined[:1])
            defined_rate = int(defined[1:])
            key = change_name(key, defined_index, defined_rate)

        length_name = len(key)
        if length_name > 16:
            key = key[:16]
        elif length_name < 16:
            for i in range(16 - length_name):
                key = key + "_"
        return key

    def pad(self, data):
        return data + (self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE) * chr(
            self.BLOCK_SIZE - len(data) % self.BLOCK_SIZE)

    def unpad(self, data):
        return data[:-ord(data[len(data) - 1:])]

    def encrypt(self, message):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(message))

    def decrypt(self, encrypted):
        key32 = self.key.encode("utf-8")
        encrypted = base64.b64decode(encrypted)
        IV = encrypted[:self.BLOCK_SIZE]
        aes = AES.new(key32, AES.MODE_CBC, IV)
        return self.unpad(aes.decrypt(encrypted[self.BLOCK_SIZE:])).decode("utf-8")
