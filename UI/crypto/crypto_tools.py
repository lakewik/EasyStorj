# import base64
import base64
import hashlib
import hmac
import storj
# import pyaes
from functools import reduce

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

from UI.resources.constants import BUCKET_META_MAGIC, BUCKET_NAME_MAGIC


class CryptoTools:

    def calculate_hmac(self, base_string, key):
        """
        HMAC hash calculation and returning the results in dictionary collection
        FROM: <https://janusznawrat.wordpress.com/2015/04/08/wyliczanie-kryptograficznych-sum-kontrolnych-hmac-plikow-i-lancuchow-znakowych/>
        """
        hmacs = dict()
        # --- MD5 ---
        hashed = hmac.new(key, base_string, hashlib.md5)
        hmac_md5 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['MD5'] = hmac_md5
        # --- SHA-1 ---
        hashed = hmac.new(key, base_string, hashlib.sha1)
        hmac_sha1 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['SHA-1'] = hmac_sha1
        # --- SHA-224 ---
        hashed = hmac.new(key, base_string, hashlib.sha224)
        hmac_sha224 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['SHA-224'] = hmac_sha224
        # --- SHA-256 ---
        hashed = hmac.new(key, base_string, hashlib.sha256)
        hmac_sha256 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['SHA-256'] = hmac_sha256
        # --- SHA-384 ---
        hashed = hmac.new(key, base_string, hashlib.sha384)
        hmac_sha384 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['SHA-384'] = hmac_sha384
        # --- SHA-512 ---
        hashed = hmac.new(key, base_string, hashlib.sha512)
        hmac_sha512 = hashed.digest().encode("base64").rstrip('\n')
        hmacs['SHA-512'] = hmac_sha512
        return hmacs

    def AES256_GCM_encrypt(self, key, iv, plaintext):
        # Generate a random 96-bit IV.
        #iv = os.urandom(12)

        # Construct an AES-GCM Cipher object with the given key and a
        # randomly generated IV.
        encryptor = Cipher(
            algorithms.AES(key),
            modes.GCM(iv),
            backend=default_backend()
        ).encryptor()

        # associated_data will be authenticated but not encrypted,
        # it must also be passed in on decryption.
        #encryptor.authenticate_additional_data(associated_data)

        # Encrypt the plaintext and get the associated ciphertext.
        # GCM does not require padding.
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        return ciphertext

    def AES256_GCM_decrypt(self, key, iv, ciphertext):
        # Construct a Cipher object, with the key, iv, and additionally the
        # GCM tag used for authenticating the message.
        decryptor = Cipher(

            algorithms.AES(key),
            algorithms.CipherAlgorithm.key_size(),
            modes.GCM(iv),
            backend=default_backend()
        ).decryptor()

        # Decryption gets us the authenticated plaintext.
        # If the tag does not match an InvalidTag exception will be raised.
        return decryptor.update(ciphertext) + decryptor.finalize()

    def prepare_bucket_entry_hmac(self, shard_array):
        storj_keyring = storj.model.Keyring()
        encryption_key = storj_keyring.get_encryption_key("test")
        current_hmac = ""
        for shard in shard_array:
            base64_decoded = str(base64.decodestring(shard.hash)) + str(current_hmac)
            current_hmac = self.calculate_hmac(base64_decoded, encryption_key)

        print current_hmac
        return current_hmac

    def encrypt_bucket_name(self, encryption_key_seed, bucket_name):
        key2 = encryption_key_seed + BUCKET_NAME_MAGIC
        sha512 = hashlib.sha512(key2)
        key_3 = sha512.hexdigest()
        sha512.update(BUCKET_META_MAGIC)
        bucket_name_key_final = sha512.hexdigest()
        bucket_name_iv, secondpart = bucket_name_key_final[:len(bucket_name_key_final)/2], bucket_name_key_final[len(bucket_name_key_final)/2:]


        data_to_encrypt = bucket_name_key_final + bucket_name_iv + bucket_name
        encrypted_bucket_name = self.AES256_GCM_encrypt(plaintext=data_to_encrypt, key=bucket_name_key_final, iv=bucket_name_iv)


        print key_3
        print bucket_name_key_final
        print encrypted_bucket_name

    def encrypt_file_name(self, encryption_key, file_name):
        return True

tools = CryptoTools()

#tools.encrypt_bucket_name("9", "kotek")


