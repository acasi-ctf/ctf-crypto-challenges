# Padding Oracle Attack
There are a few things to keep in mind before going deeper into the topic:
1. The last block is always padded
2. `plaintext[i - 1] = cipher[i – 1] ⨁ Dec(K, cipher[i])`
3. `A ⨁ A = 0`
4. `0 ⨁ A = A`
5. The decryption algorithm will throw an invalid padding error when the `plaintext[i – 1]` it decrypted does not have a valid padding.


*Without other protection, padding could possibly leak the entire message’s content.*

## Notation wise:
- Let the last ciphertext block to be C
- Let the second last ciphertext block to be C’
- Let C[i] denotes the i’th byte of the block C, starting from 0
- Let size of each block to be N

## Let’s see how we can get the last byte:
1. There are 2 ways that a ciphertext can be decrypted without throwing an invalid padding error
   1.  Decrypt the ciphertext without modifying it
   2.  Set the last byte to be 01
2. We want to make use of the property `1.2`.
	- Recall the last step to decrypt a block is xoring with the previous ciphertext block
	- We have edit access to the ciphertext block
	- ### Aim: Edit C’[N-1] such that C^' [N-1]⨁Dec(K,C[N-1])=01
	    - We know that, without any modification `C'[N-1] ⨁ Dec(K,C[N-1]) = A`, where A is the original value
	    - What if we make `C'[N-1] ⨁ A ⨁ 01` to be the second last block.
    	    - Based of the xor property, it will output `01` which will not throw an invalid padding error
	    - Now, we only need to find A.
        	- We know that there are 2 output values that will not make the decryption algorithm to throw an invalid padding error
	            1. 01, i.e. If we make the second last block to be `C'[N-1] ⨁ A ⨁ 01`
	            2. A, i.e. If we make the second last block to be `C'[N-1] ⨁ 01 ⨁ 01 = C'[N - 1]`
	        - We just need to xor `C’[N-1]` with all possible values `from 02 to FF` and send to the decryption algorithm to find the only value that does not throw an invalid padding error.
    	        - The value will be A. 
    	        - 256 trials per byte


### How can we extend this to get all other bits?
- Note: we already found out the last byte. We need to find the second last byte. What are the values that the last 2 bytes can take such that they will not cause an invalid padding error?  
