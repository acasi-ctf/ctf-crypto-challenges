# CTF Crypto Challenges

This repository has the cryptographic challenges we implemented.

The challenges are divided based on their type/characteristic.

# Topics Involved:

## Confidentiality:

### Symmetric Encryption 
    We have all of the documentation written, some are not implemented
- #### One Time Pad (OTP)
  1. Introduction to the algorithm (Basic Encryption and Decryption)
  2. Problems/weakness (Using the same key twice)
  - Note: These 2 challenges are written in Python. However, it works the best in web-interface. User only need to give their final answer.

- #### Block Cipher
  1. Introduction to the algorithm (Basic Encryption and Decryption)
  2. Brute Forcing the algorithm
  3. Meet in the middle attack (Not implemented):
     1. This is not possible with the current setup.
     2. We need a place for user to submit their answer and a place for user to write some python code using the functions we have written.
     3. We have documented down its background_info and challenge description
  - Note: Challenge 1 and 2 are written in Python, but similar to OTP, were designed to be implemented as a web-section.
  - Note: Challenge 3 needs user to have access to the terminal and write their own code (using the provided .py library) and a place for them to submit their answers. It's not possible to let them download/copy the provided code because other `.py `libraries will be used here. (Unless we want them to `pip ___`, that defeats the purpose of this project.)

- #### Modes of Operation (Encryption messages of variable size)
  - #### Electronic Code Book (ECB) (Not implemented yet)
    1. Introduction to the algorithm (Basic Encryption and Decryption)
    2. Dictionary/Frequency attack
    - Note: These 2 challenges, like OTP, work the best in web-interface

  - #### Counter Mode Encryption
    1. Introduction to the algorithm (Simple Encryption and Decryption)
    2. Weakness (Using the same invitial value/vector)
    - Note: These 2 challenges work the best in web-interface

  - #### Cipher Block Chaining (Not implemented)
    1. Introdcution to the algorithm
    2. Padding and Padding Oracle Attack
        1. Similar to Meet in the middle attack, this requires a place for user to submit their answer and for them to write python code to break the encryption.
    
### Asymmetric Encryption (Public key encryption) (Not implemented)
    Not started yet.

- #### Modular Arithmetic
  - Properties
  - Generators and groups
  - Note: This is needed to understand Asymmetric Encryption.

- #### RSA
  1. Introduction to RSA (Math-like challenges)
     - How to find the large number N
     - How to find the inverse
     - How to make use of the modular arithmetic properties to encrypt and decrypt
  2. Breaking it by frequency analysis or dictionary attack (It is deterministic if we are using the same generator all the time)

  3. Diffie-Hellman Key Exchange Algorithm
     - Using RSA to exchange symmetric encryption keys


## Integrity
  0. ### Definition of Integrity
     - Challenges that let user to clear distinguish integrity from confidentiality  

  1. ### Message Authentication Code (MAC)
     - Introduction to the idea
  
  2. ### MAC of a variable length message
     - #### CBC MAC
       - Introduction to the algorithm
       - Break it by appending other messages

     - #### ECBC - MAC
       - Outline the differences between this and CBC MAC
       - Simple challenges that ask user to obtain MAC of a message (with provided python starter code)
  
  3. ### Hashing
      - Introducing HASH and its requirement
      - Weakness: Attack a simple hash function (16 bits) using dictionary attack
      - Why Hash alone cannot be used as a MAC

  4. ### HMAC (Hashing then MAC)
     - MAC variable length messages


## Confidentiality and Integrity
  1. Encrypt and MAC
  2. Encrypt then MAC
  3. MAC then Encrypt
  - Note: For each one of these, explain how it works and its weaknesses. 