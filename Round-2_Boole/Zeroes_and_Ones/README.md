# Zeroes and Ones

### Challenge
> ***Bit String Flicking***
> How many solutions are there for X in the expression:
> LCIRC -3 (01011 AND X OR 10100) = 01101


### Hint
> Try simplifying it?

### Solution
I refered to these 2 links which explain how bit string flicking works
- http://stackoverflow.com/questions/35161385/acsl-bit-string-flicking
- http://www.apcomputerscience.com/cst/topic_descriptions/bitStringFlicking.pdf

Using what I've just learnt, let's simplfy this first.

	LCIRC -3 (01011 AND X OR 10100) = 01101
	(01011 AND X OR 10100) = RCIRC-3(01101)
	(01011 AND X OR 10100) = 10101

According to the above references, order of operation: NOT, SHIFT, CIRC, AND, XOR, OR
So, continuing on...

	(01011 AND X) OR 10100 = 10101
	(01011 AND X) = x0x01

Taking a look at `01011`, it is masking away index 2 and index 4 bits.
Since those 2 bits are "don't care", there will be 2^2 = 4 possible values of X.

Thus, the flag is `4`