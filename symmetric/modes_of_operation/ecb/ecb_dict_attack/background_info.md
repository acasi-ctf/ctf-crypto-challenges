# Electronic Code Block Weakness
ECB is deterministic. i.e. On a given input, it will always have the same output. 

It leaves plaintext data patterns in the ciphertext and creates opportunities for frequency analysis. 

Typical example is encrypting images using ECB: 

["ecbEncrypted"](ecbEncrypted.png)


Since the algorithm is deterministic, it is extremely easy to forge messages. 