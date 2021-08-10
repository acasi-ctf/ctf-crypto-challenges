# This python file runs the second challenge of counter mode encryption
import flawed_encryption as flawed
import time

# prompts
def prompt1():
    print("Alice and Bob are sending longer messages and chose to use CTR mode encryption.")
    print("You had the chance to use Alice’s computer and send the following message to Bob:")
    print()
    print("Hi, how are you doing today? Are we going to meet this afternoon")
    print()
    print("You've intercepted the encrypted message:")
    print()

# setup the given and secret messages
# key and ciphertext
def setup():
    msg_known = "Hi, how are you doing today? Are we going to meet this afternoon"

    msg_secret = "I'm going to send you the $100, please give me your bank account"

    key = flawed.key_gen()

    encrypted = flawed.encrypt(key, msg_known, 0)
    print(encrypted.hex())

    return msg_secret, key

# the challenge starts here
def test(key, msg_secret):
    print()
    time.sleep(3)
    print("You intercepted Alice's message to Bob. Here is the ciphertext:")
    print()
    encrypted = flawed.encrypt(key, msg_secret, 0)
    print(encrypted.hex())
    print()
    print("Try to decrypt it and see what the message is:")
    ans = input("Type your answer here: ")
    while (ans != msg_secret) :
        print("That doesn't seem right.")
        input("Try again: ")
    print("You are correct!")
    print("Challenge is going to be closed in 3 seconds")
    time.sleep(3)

prompt1()
msg, key = setup()
test(key, msg)


    

