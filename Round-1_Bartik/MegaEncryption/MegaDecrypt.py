#!/usr/bin/env python
from base64 import b64decode 

with open("MegaEncrypted_message.txt", "r") as file:
    input = file.read().strip()

iter = 0
while "MegaEncryption" not in input:
    input = b64decode(input).strip()
    iter += 1

print "iter =", iter 
print input