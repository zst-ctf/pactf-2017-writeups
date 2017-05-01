
def ascii_to_hex_str(text):
	#return "".join("{:02x}".format(ord(c)) for c in text)
	return "".join(("%02x" % ord(c)) for c in text)


def hex_int_to_ascii(text):
	text = hex(text) # convert int to hex string
	text = text[2:]  # remove prefix 0x
	if text.endswith("L"):
		text = text[:-1]  # remove suffix L
	print text
	return text.decode("hex") # decode the hex string to ascii