## Why can't we reuse keys?

We can't reuse keys because given two ciphertexts that were generated with the same key, someone could XOR the ciphertext to gain information about both messages. Although they won't be able to perfectly reconstruct the plaintext, they will be able to access enough information to the point that it is dangerous.

Look at these sources for good visuals on how dangerous this is:
- [James Stanley Blog on OTP Key Reuse](https://incoherency.co.uk/blog/stories/otp-key-reuse.html)
- [StackExchange Post on OTP Key Reuse](https://crypto.stackexchange.com/questions/59/taking-advantage-of-one-time-pad-key-reuse)

## One Time Pad Requirements
From the previous section, we learned about the dangers of key reuse. There are more
things that we need to keep in mind to ensure that OTP is safe. To guarantee the perfect secrecy of OTP, the following requirements must be maintained (source: [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad)):

1. The key must be random (uniformly distributed and independent of the plaintext).
2. The key must be at least as long as the plaintext.
3. The key must never be reused in whole or in part.
4. The key must be kept completely secret by the communicating parties.

## Learn more
- [Wikipedia](https://en.wikipedia.org/wiki/One-time_pad)
- [James Stanley Blog on OTP Key Reuse](https://incoherency.co.uk/blog/stories/otp-key-reuse.html)
- [StackExchange Post on OTP Key Reuse](https://crypto.stackexchange.com/questions/59/taking-advantage-of-one-time-pad-key-reuse)
