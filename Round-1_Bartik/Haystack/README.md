# Haystack

### Challenge
> That’s a lot of data… but at least it’s signed! I’ll bet that at least one signature doesn’t match up, though. One of ‘em has a bit of cuil. It’ll be like finding a needle in a haystack…
> haystack.json

### Hint
> Yes, I know that the RSA key format doesn’t really matter in this scenario (considering there isn’t much of a format).

### Solution
Thankfully, everything is nicely arranged in a JSON. I created a python script to verify each of the signature and data. It uses the PyCrypto library and [this code by @lkdocs](https://gist.github.com/lkdocs/6519372). The script will print the entry which does not successfully verify.

    3314 False
    Signature: VQEuLxEcKQt7z3prMCTnuf4vuR8UyQGdPcssw0Nezi5J2OSNPLfpi154Yn/dqCDUBkuJt1HfUOuswPAziRx/1KesXhf4j5dIDx65gk2UtuVEVazLoaG9UEbFJGXhONUdCb4CO/6O30hI8I37JNTAr+ilLDczKGNzWb59DX6aBHI=
    Data: WW91IGZvdW5kIGl0ISBGbGFnOiBzb21ldGltZXNfbmVlZGxlc19pbl9hX2hheXN0YWNrX2Nhbl9wcmlja195b3U=

Since the data is base-64 encoded, I suspect the flag is in there. Paste the data into [this online tool](https://www.base64decode.org/) and we get the flag!
    
    You found it! Flag: sometimes_needles_in_a_haystack_can_prick_you