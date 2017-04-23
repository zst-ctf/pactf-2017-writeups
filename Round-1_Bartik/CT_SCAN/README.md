# CT S(C)AN

### Challenge
> CHECK THE SAN. MAYBE CT SCANS ARE USEFUL TOO

### Hint
> We are a security competition, not a hospital. Consult with your healthcare professional before deciding to take any CAT scans.

### Solution

Going through pages and pages of searching, [I found this page which implies that CT means certificate](https://www.entrust.com/protect-domain-ct-search/)

Afterwhich, I searched for `checking certificate SAN` which yielded me this [StackOverflow thread](http://stackoverflow.com/questions/13127352/how-to-check-subject-alternative-names-for-a-ssl-tls-certificate). 

Using their code, run this in command line:

    openssl s_client -connect 2017.pactf.com:443 | openssl x509 -noout -text | grep DNS:

The result is:
    
    DNS:2016.pactf.com, DNS:2017.pactf.com, DNS:pa1cdnp5ocrn977rcqy98ubvkq92o5-flag.pactf.com, DNS:pactf.com, DNS:splash.pactf.com, DNS:status.pactf.com, DNS:www.pactf.com

Hence, the flag is `pa1cdnp5ocrn977rcqy98ubvkq92o5`