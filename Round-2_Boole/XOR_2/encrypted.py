with open("Article.txt", "r") as file:
	input = file.read()

enc_ascii = input.decode("hex")

enc_numbers = [ord(ch) for ch in enc_ascii]
