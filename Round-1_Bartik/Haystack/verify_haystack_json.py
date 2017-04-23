#!/usr/bin/env python
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64decode 
import json

'''
Original dode by lkdocs
    https://gist.github.com/lkdocs/6519372
Slightly modified
'''
def verify_sign_direct(pub_key, signature, data):
    '''
    Verifies with a public key from whom the data came that it was indeed 
    signed by their private key
    param: public_key_loc Path to public key
    param: signature String signature to be verified
    return: Boolean. True if the signature is valid; False otherwise. 
    '''
    rsakey = RSA.importKey(pub_key) 
    signer = PKCS1_v1_5.new(rsakey) 
    digest = SHA256.new() 
    # Assumes the data is base64 encoded to begin with
    digest.update(b64decode(data)) 
    if signer.verify(digest, b64decode(signature)):
        return True
    return False

# http://stackoverflow.com/questions/40094108/i-have-a-rsa-public-key-exponent-and-modulus-how-can-i-encrypt-a-string-using-p
modulus = 132014992946851317628321108822184364863563257578174555813409401134257485091016568808351080087191570957978528479437568482885991726617458842578017613352322660969645156597141779386157600232772803000093782179823643344946683602358622484533804213014960185007035142552526386910993194802007914025290782677761336471601
e = 65537L
n = modulus
# http://stackoverflow.com/questions/34279901/python-rsa-encryption
pubkey = construct((n, e)).exportKey()
#print pubkey

haystack_str = open("./haystack.json", "r").read();
data = json.loads(haystack_str)['haystack']

for count, item in enumerate(data):
    signature = item['signature']
    data = item['data']
    result = verify_sign_direct(pubkey, signature, data)
    if result is False:
        print count, result
        print "Signature:", signature
        print "Data:", data
