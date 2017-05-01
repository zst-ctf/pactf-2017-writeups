#!/usr/bin/env python
import re
import sys
from itertools import cycle, izip

with open("Article.txt", "r") as file:
	input = file.read()

text = input.decode("hex")

def apply_xor(message, key):
	# http://stackoverflow.com/questions/42921162/xor-cipher-decryption
	cryptedMessage = ''.join(chr(ord(c)^ord(k)) for c,k in izip(message, cycle(key)))
	return cryptedMessage

def hex_int_to_ascii(text):
	text = hex(text) # convert int to hex string
	text = text[2:]  # remove prefix 0x
	if text.endswith("L"):
		text = text[:-1]  # remove suffix L
	if len(text) % 2 != 0:
		text = "0" + text
	## print text
	return text.decode("hex") # decode the hex string to ascii

'''
	Did you know that in typical English writing, a 
	character is the same as the one k characters in
	front of it about 8% of the time, regardless of k?
'''
def check_english_probability(input, k=7, start=0):
	# Python slice http://stackoverflow.com/a/20847228
	chars = input.lower()[::k]
	## print chars
	total_count = len(chars)
	k_count = chars.count(chars[start])
	probability = k_count * 100.0 / total_count

	#print "probability =", probability

	if 7 < probability < 9:
		print "probability =", probability
		return True
	return False

for i in xrange(0xFF, 0xFFFFFFFFFFFFFFF):
	if (i & 0xFF == 0xFF):
		print "progress = %x" % i
	output = apply_xor(text, hex_int_to_ascii(i))
	if check_english_probability(output):
	#if "{" not in output:
		print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ xor =", i
		print output
		sys.exit()




'''
>>> one_time_pad = 'shared secret' 
>>> plaintext = 'unencrypted' 
>>> ciphertext = xor(plaintext, one_time_pad) 
>>> ciphertext 
bytearray(b'\x06\x06\x04\x1c\x06\x16Y\x03\x11\x06\x16') 
>>> decrypted = xor(ciphertext, one_time_pad) 
>>> decrypted
bytearray(b'unencrypted')
>>> plaintext == str(decrypted)
True
'''