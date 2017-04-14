############ Module with cryptographics functions for Storj GUI Client ##########
## Based on: <http://stackoverflow.com/questions/16761458/how-to-aes-encrypt-decrypt-files-using-python-pycrypto-in-an-openssl-compatible> ##

from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random


class FileCrypto:

    def encrypt_file(self, algorithm, file_path, encrypted_file_save_path, password):
        if algorithm == "AES":
            with open(file_path, 'rb') as in_file, open(encrypted_file_save_path, 'wb') as out_file:
                self.encrypt_file_aes(in_file, out_file, password)

    def decrypt_file(self, algorithm, file_path, decrypted_file_save_path, password):
        if algorithm == "AES":
            with open(file_path, 'rb') as in_file, open(decrypted_file_save_path, 'wb') as out_file:
                self.decrypt_file_aes(in_file, out_file, password)

    def derive_key_and_iv(self, password, salt, key_length, iv_length):
        d = d_i = ''
        while len(d) < key_length + iv_length:
            d_i = md5(d_i + password + salt).digest()
            d += d_i
        return d[:key_length], d[key_length:key_length + iv_length]

    def encrypt_file_aes(self, in_file, out_file, password, key_length=32):
        bs = AES.block_size
        salt = Random.new().read(bs - len('Salted__'))
        key, iv = self.derive_key_and_iv(password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        out_file.write('Salted__' + salt)
        finished = False
        while not finished:
            chunk = in_file.read(1024 * bs)
            if len(chunk) == 0 or len(chunk) % bs != 0:
                padding_length = bs - (len(chunk) % bs)
                chunk += padding_length * chr(padding_length)
                finished = True
            out_file.write(cipher.encrypt(chunk))

    def decrypt_file_aes(self, in_file, out_file, password, key_length=32):
        bs = AES.block_size
        salt = in_file.read(bs)[len('Salted__'):]
        key, iv = self.derive_key_and_iv(password, salt, key_length, bs)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        next_chunk = ''
        finished = False
        while not finished:
            chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024 * bs))
            if len(next_chunk) == 0:
                padding_length = ord(chunk[-1])
                if padding_length < 1 or padding_length > bs:
                    raise ValueError("bad decrypt pad (%d)" % padding_length)
                # all the pad-bytes must be the same
                if chunk[-padding_length:] != (padding_length * chr(padding_length)):
                    # this is similar to the bad decrypt:evp_enc.c from openssl program
                    raise ValueError("bad decrypt")
                chunk = chunk[:-padding_length]
                finished = True
            out_file.write(chunk)
