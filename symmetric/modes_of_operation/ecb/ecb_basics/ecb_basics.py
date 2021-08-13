# This python program implements the basic encryption and decryption
# challenge of ecb

import ecb_lib as lib

def challenge1():
    key = lib.key_gen(6)
    
    msg = "ABC" #change the msg here
    blocksize = lib.block_size_gen(len(msg))
    cipher = lib.encrypt(msg, blocksize, key) 
    print("The Key is :", key)
    print("The block size is :", blocksize)
    lib.encryption_test(cipher)

    print("You've received a message from James: ")
    msg = "ABC" #change this msg
    new_key = lib.key_gen(6)
    new_blocksize = lib.block_size_gen(len(msg))
    cipher = lib.encrypt(msg, new_blocksize, new_key)

    print("The New Key is :", new_key)
    print("The new block size is :", new_blocksize)
    print("The ciphertext is:", cipher)
    lib.decryption_test(msg)

challenge1()
