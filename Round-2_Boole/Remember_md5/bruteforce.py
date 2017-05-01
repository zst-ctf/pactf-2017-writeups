#!/usr/bin/env python
## http://stackoverflow.com/a/11747381
## http://stackoverflow.com/questions/5297448/how-to-get-md5-sum-of-a-string

import hashlib
import sys

target_hash = "1b657b7fe26eda5b3c1309d340f1674d"
characters = ['a', 'b', 'c']
permutations = []

# Get all permutations possible with the characters
a = characters
for y in xrange(14):
    a = [x+i for i in characters for x in a]
permutations = a

# For each of the possibilities, run it through md5
# and check if it is equal to our target.
# Break out and print once it is correct
for each in permutations:
    if hashlib.md5(each).hexdigest() == target_hash:
        print each
        sys.exit()