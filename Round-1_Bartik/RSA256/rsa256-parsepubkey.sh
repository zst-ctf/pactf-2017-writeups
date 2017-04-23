#!/usr/bin/env sh
# http://dann.com.br/alexctf2k17-crypto200-poor_rsa/
PUB_KEY="MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAIl47p5SrV3uMTsUAbwE0E+j+QynAY/CVq/Gf8IAOQy7AgMBAAE="
echo $PUB_KEY | base64 --decode | openssl asn1parse -inform DER -i -strparse 17