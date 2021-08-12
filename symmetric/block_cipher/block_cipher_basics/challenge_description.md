# Block Cipher: Encryption and Decryption

You and your friend James are trying to send a secret message to each other. Both of you have access to the key, which you will use to encrypt and decrypt each other’s messages. You want to send the following message to James: 

**<insert msg>**

Encrypt the message to prevent other people from knowing.
  

Below is the Simple Block Cipher Key-Plaintext-Ciphertext table:

| Input | K = 0 | K = 1 | K = 2 | K = 3 | K = 4 | K = 5 | K = 6 | K = 7 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0     | 12    | 2     | 6     | 12    | 15    | 15    | 2     | 12    |
| 1     | 6     | 0     | 15    | 0     | 11    | 10    | 7     | 5     |
| 2     | 10    | 14    | 2     | 14    | 6     | 8     | 14    | 11    |
| 3     | 15    | 1     | 7     | 4     | 3     | 5     | 4     | 10    |
| 4     | 14    | 5     | 12    | 8     | 1     | 7     | 11    | 3     |
| 5     | 0     | 13    | 11    | 11    | 8     | 14    | 0     | 7     |
| 6     | 11    | 10    | 0     | 2     | 14    | 6     | 3     | 1     |
| 7     | 1     | 9     | 9     | 7     | 9     | 3     | 10    | 9     |
| 8     | 4     | 6     | 4     | 6     | 5     | 0     | 6     | 15    |
| 9     | 7     | 4     | 14    | 9     | 2     | 12    | 9     | 13    |
| 10    | 5     | 8     | 8     | 13    | 7     | 11    | 8     | 14    |
| 11    | 8     | 7     | 13    | 15    | 12    | 1     | 13    | 0     |
| 12    | 9     | 11    | 10    | 3     | 13    | 13    | 5     | 8     |
| 13    | 13    | 12    | 5     | 1     | 0     | 4     | 12    | 4     |
| 14    | 2     | 3     | 1     | 5     | 4     | 9     | 15    | 6     |
| 15    | 3     | 15    | 3     | 10    | 10    | 2     | 1     | 2     |
