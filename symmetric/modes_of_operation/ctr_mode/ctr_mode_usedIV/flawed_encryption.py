from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def key_gen() :
    return get_random_bytes(16)

def encrypt(key, msg, iv):
    aes = AES.new(key, AES.MODE_CTR, initial_value=iv, nonce=b"0")
    ciphertext = aes.encrypt(msg.encode("utf8"))

    return ciphertext

def decrypt(key, cipher, iv, aes_algo):
    plaintxt = aes_algo.decrypt(cipher)

    return plaintxt.decode("utf-8")