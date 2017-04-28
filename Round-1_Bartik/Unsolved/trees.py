'''
with open("test.png", "rb") as imageFile:
  f = imageFile.read()
  b = bytearray(f)

chararr = map(lambda x: chr(x), b)
print ''.join(chararr)
print ','.join(map(lambda x: str(x), b)
)

'''
# http://stackoverflow.com/questions/11064786/get-pixels-rgb-using-pil


import binascii
def bin2ascii(input):
    n = int(input, 2)
    return chr(n)
    #return binascii.unhexlify('%x' % n)

from PIL import Image
im = Image.open('trees.png', 'r')
width, height = im.size
pixel_values = list(im.getdata())
#print pixel_values
bin = ""
for i, pix in enumerate(pixel_values):
    if True:#(i % 8) == 0:
        bin += str(pix[2] & 0x1) 

print "count i =", i

import re
listBin = re.findall('.{8}', bin)
out = ""
for i, ch in enumerate(listBin):
    if (i % 8) == 0:
        out += bin2ascii(ch)
print out

#print bin2ascii(bin)
#print bin
'''
pixel_values_nodup = set(pixel_values)
print pixel_values_nodup
'''