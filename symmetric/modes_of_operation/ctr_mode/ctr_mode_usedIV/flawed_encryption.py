from Crypto.Cipher import AES
import random

def key_gen() :
    return random.getrandbits(128)

def encrypt(key, msg, iv):
    aes = AES.new(key, AES.MODE_CTR, initial_value=iv)
    ciphertext = aes.encrypt(msg)

    return ciphertext.hex()

def decrypt(key, cipher, iv):
    aes =AES.new(key, AES.MODE_CTR, initial_value=iv)
    plaintxt = aes.decrypt(cipher)

    return plaintxt.decode("utf-8")

# for testing purpose
pt = "Hello, how is it going? Wanna get a drink?"
key = key_gen()

ci = encrypt(key, pt, 0)
print(ci)

de = decrypt(key, ci, 0)
print(de)



