# Hash Killer

### Challenge
> Qu’est que c’est?
> We were clearing out the old server and came across a really weird [file](hashes.txt)…

### Hint
> Did someone say MD5? And that last line seems different from the rest…

### Solution
The hint tells us all lines except the last are MD5.
Running it through a [MD5 decrypter](https://hashkiller.co.uk/md5-decrypter.aspx), we get a taunting message

	oh you wish it were this easy ? 
	sorry to let you down but this rabbit hole goes deeper !
	the word 'AES' hash is the key now decrypt me START

The message tells us it is AES, I'm guessing it is the commone AES in ECB mode.
The message tells us that the key is the MD5 hash of 'AES'
The last line of the file seems to be the base-64 encoded ciphertext.

I copied and modified [a Python script written by @LFlare](https://github.com/LFlare/picoctf_2017_writeup/blob/master/cryptography/computeaes/decrypt.py) for my use. Python Script
Finally, we get the flag in the output `flag{w3_l0v3_3ncrypt10n}`
*(See the [Python script](hash_killer_solved.py))*
