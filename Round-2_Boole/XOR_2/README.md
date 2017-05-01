# XOR 2

### Challenge
> Miles just sent me a really cool article to read! Unfortunately, he encrypted it before he sent it to me. Can you crack the code for me so I can read the article? [Article.txt](Article.txt)

### Hint
> Did you know that in typical English writing, a character is the same as the one k characters in front of it about 8% of the time, regardless of k?

### Solution
I tried bruteforcing according to the hint and checking for the 8%, but it proved to be too time-consuming.
After reading up on solving XOR ciphers, I came across [Kasiski examination](https://en.wikipedia.org/wiki/Kasiski_examination) and frequency analysis.

I found a [picoCTF 2014 writeup by Gladius Maximus](https://ehsandev.com/pico2014/cryptography/repeated_xor.html) which has a solution to solve repeated XOR ciphers using Kasiski examination and frequency analysis.

The script can be used as it, but we need to modify `encrypted.py` to point to our article.

	with open("Article.txt", "r") as file:
		input = file.read()

	enc_ascii = input.decode("hex")

Now we have that, let's run `kasiski.py`. This gives us key-length 12 as the highest probability:

	 12 | 827 |==============================================================================================================================================================================================================

Now we need to change the key length used for the decryption in `kasiski.py`

	key_len = 12

Let's run `kasiski.py` again and we get our article! [output.txt](output.txt)
This sentence is inside the article.

	The flag is primes_are_cool.