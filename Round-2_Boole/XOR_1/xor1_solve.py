#!/usr/bin/env python
import re

text = "KGZFK\qZFG]qA\qZFOZ"

def apply_xor(ch, key):
	return chr(ord(ch) ^ key)

for i in range(255):
	print "".join(apply_xor(ch, i) for ch in text)