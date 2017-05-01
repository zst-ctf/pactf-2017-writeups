# XOR 1

### Challenge
> My friend Miles sent me a secret message. He said he encoded it with an XOR cipher. Can you figure out what his message “KGZFK\qZFG]qA\qZFOZ” means?

### Hint
> The key is only one digit long

### Solution

[Reading Wikipedia on XOR cipher](https://en.wikipedia.org/wiki/XOR_cipher), each of the characters can be encrypted with a repeating key. Hence, we apply an XOR key to each of the characters. *(See the [Python script](xor1_solve.py))*

Since each ASCII character is 8-bits long, we can bruteforce all the XOR keys from 0 - 255. 

When we look at the output, we see 2 intelligible strings.
	
	EITHERTHISORTHAT

	either_this_or_that

Trying both of it, the flag is `either_this_or_that`.