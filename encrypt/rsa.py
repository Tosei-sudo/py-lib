# coding: utf-8
from math2 import gcd, lcm
import hashlib
import random
import struct

def generate_keys(p, q):
    '''
    与えられた 2 つの素数 p, q から秘密鍵と公開鍵を生成する。
    '''
    N = p * q
    L = lcm(p - 1, q - 1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    return RSAKey(E, N), RSAKey(D, N)

class DecryptionError(Exception):
    pass

class EncryptionError(Exception):
    pass

class RSAKey(object):
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2

    def get_binary(self):
        return struct.pack('!II', self.key1, self.key2)

class RSA(object):
    def __init__(self, p, q):
        self.public_key, self.private_key = generate_keys(p, q)

    def encrypt(self, plain_text):
        '''
        公開鍵 public_key を使って平文 plain_text を暗号化する。
        戻り値は暗号化されたintegersのリスト。
        '''
        try:
            if type(plain_text) == unicode:
                plain_text = plain_text.encode('utf-8')
            
            plain_random = random.randint(0, 255)
            plain_body = [ord(byte) ^ plain_random  for byte in plain_text]
            plain_body_hash = [ord(byte) for byte in hashlib.sha256(plain_text).digest()]
            
            plane_data = [plain_random]
            plane_data.extend(plain_body)
            plane_data.extend(plain_body_hash)
            
            encrypted_integers = [pow(i, self.public_key.key1, self.public_key.key2) for i in plane_data]

            return struct.pack('!%dI' % len(encrypted_integers), *encrypted_integers)
        except Exception as e:
            raise EncryptionError('Encryption failed')

    def decrypt(self, encrypted_data):
        '''
        秘密鍵 private_key を使って暗号文 encrypted_text を復号する。
        '''
        try:
            encrypted_integers = struct.unpack('!%dI' % (len(encrypted_data) / 4), encrypted_data)
            
            decrypted_integers = [pow(i, self.private_key.key1, self.private_key.key2) for i in encrypted_integers]
            
            decrypted_random = decrypted_integers[0]
            decrypted_body = decrypted_integers[1:-32]
            decrypted_hash = decrypted_integers[-32:]
            
            decrypted_text = ''.join(chr(i ^ decrypted_random) for i in decrypted_body)
            
            decrypted_text_hash = hashlib.sha256(decrypted_text).digest()
            decrypted_hash_str = ''.join(chr(i) for i in decrypted_hash)
            
            if decrypted_hash_str != decrypted_text_hash:
                raise DecryptionError('Hash mismatch')
            
            decrypted_text = decrypted_text.decode('utf-8')
            return decrypted_text
        except Exception as e:
            raise DecryptionError('Decryption failed')