# This challenge will show how vulnerable ecb is
import ecb_lib as lib
import time

def challenge2():
    key = lib.key_gen(6)
    
    msg = "ABC" #change this msg
    blocksize = lib.block_size_gen(len(msg))
    cipher = lib.encrypt(msg, blocksize, key) #Change this msg
    print("You are sitting besides Alice and you see her msg to Bob:", msg)
    print("The CipherText that you intercepted :", cipher)

    time.sleep(3)

    msg = "ABC" #Change this msg

    cipher = lib.encrypt(msg, blocksize, key)
    print("You intercepted a message sent from Bob to Alice!")
    print("The Ciphertext is :", cipher)

    lib.decryption_test(msg)

challenge2()