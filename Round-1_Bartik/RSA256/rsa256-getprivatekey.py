# References:
#     https://simple.wikipedia.org/wiki/RSA_(algorithm)#Operation
#     http://dann.com.br/alexctf2k17-crypto200-poor_rsa/
#     https://github.com/VulnHub/ctf-writeups/blob/master/2017/alexctf/crypto4.md

from Crypto.PublicKey import RSA

# Mod-inverse code by ofaurax
#     https://gist.github.com/ofaurax/6103869014c246f962ab30a513fb5b49
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

# http://stackoverflow.com/questions/16310871/in-rsa-encryption-how-do-i-find-d-given-p-q-e-and-c
# p and q retrieved from www.factordb.com
# Formula for d = e.modInverse(p_1.multiply(q_1))

n = 62180528787689937819999198320875604188782593051291064364537897810852251765947
e = 65537L
p = 224258454597761606450883324956139951511
q = 277271726050281009396301232126405463677
phi = (p-1) * (q-1)
d = modinv(e, phi)

# http://stackoverflow.com/questions/33337904/rsa-generate-private-key-from-data-with-python
private_key = RSA.construct((n,e,d)).exportKey()
print private_key