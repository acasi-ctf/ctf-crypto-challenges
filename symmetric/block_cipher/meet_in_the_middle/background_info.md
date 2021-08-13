# Meet in the middle
As computing powers becomes stronger, DES that uses 56-bit key could be broken within a few hours.
A possible way to make it harder to break, apart from using a longer key or changing to AES, is using 3 DES.

## 3 DES (needs 2 56-bits keys)
-	To encrypt:
    1. Encrypt with DES the plaintext using Key1 to get C1.
    2. Decrypt C1 with Key2 to get C2.
    3. Encrypt C2 with Key1 to get the final ciphertext.
   
-	To decrypt:
	1. Decrypt the ciphertext with Key1 to get C2.
	2. Encrypt C2 with Key2 to get C1.
	3. Decrypt C1 with Key1 to get the plaintext.

Another possible suggestion is to use 2 DES

## 2 DES (Safe/Secure?)
Proposed encryption algorithm:
1. Encrypt the plaintext with Key1 to get C1.
2.  Encrypt C1 with Key2 to get the final ciphertext.

There are, in total, `2^N * 2^N = 2^(2N)` key combinations where N = key length.
Is there are faster way to break this Encryption algorithm without looping through all possible key combinations? (Hint: Look at C1 and think about decryption)