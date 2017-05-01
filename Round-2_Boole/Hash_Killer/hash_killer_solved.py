#! /usr/bin/env python
import base64
from Crypto.Cipher import AES
import hashlib

key = hashlib.md5("AES").hexdigest()
ciphertext = base64.b64decode("mJRKaaMSR1atUGs0kOkAJP3dty9tjCvXKMzWDHtZdRQ=")
text = AES.new(key, AES.MODE_ECB).decrypt(ciphertext)
print text