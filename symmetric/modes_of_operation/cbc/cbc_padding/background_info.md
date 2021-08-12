# Padding in CBC
## When do we need to do padding?
Since we need to pass Temp through a block cipher using the same key, K, all the Temps must have the same length. This means that length of the plaintext must be a multiple of N, where N is the length of a block.

## How do we pad the last block?
### First attempt: Using 0 at the end of the block
Qn: How can we distinguish the padded 0 from the actual value 0?

### Byte Padding: Block size is in bytes

#### PKCS#5 and PKCS#7:
Instead of using 0, we pad each byte with the value of total number of bytes added.
- e.g: 
  - If we only need to pad 1 byte, we will pad `01` at the end
  - 2 byte: `02 02`
  - 3 byte: `03 03 03`

### Example1:
Suppose the message is
 - `… | AB 12 19 9C 11 05 F3 D4 | 5E 06`
 - Block size = 8 bytes 

The last block has a size of only 2 bytes:
  - We need to pad 6 bytes to the last block, so the value to pad is 06

Therefore, the padded message will be:
  - `… | AB 12 19 9C 11 05 F3 D4 | 5E 06 06 06 06 06 06 06`
  - Note: there are 7 `06`’s at the end of the last block, the first one is part of the message.


### Message length = mulitple of N
If the original message’s length is a multiple of N, where N is the block size, an extra block filled with N with be added to the end of the message
- e.g. For message like
    - `… | AB 12 19 9C 11 05 F3 D4 | 5E 06 12 51 0E AF BB 9D`

Which has all blocks filled. The padded message will be
  - `… | AB 12 19 9C 11 05 F3 D4 | 5E 06 12 51 0E AF BB 9D|08 08 08 08 08 08 08 08`


This is to make the last block to always be a padded block. Why is this needed?

### After Padding:

We will then encrypt this padded message using CBC.
