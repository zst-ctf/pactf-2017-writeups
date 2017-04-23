# RSA256

### Challenge
> According to [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Integer_factorization_and_RSA_problem), RSA 256 can be factored on modest hardware in 35 minutes. Given the encoded public key `MDwwDQYJKoZIhvcNAQEBBQADKwAwKAIhAIl47p5SrV3uMTsUAbwE0E+j+QynAY/CVq/Gf8IAOQy7AgMBAAE=`, what is the similarly-encoded private key? The first 32 characters is the flag.

### Hint
> And apparently YAFU can do it in 103 seconds!

### Solution

*The shell script and python script I used are in this folder. Sources from where I've copied the codes are commented in too!*

Firstly, we are given a base-64 encoded public key, we need to parse it and retrieve the exponent `e` and modulus `n`.
This is the result after conversion

    2:d=1  hl=2 l=  33 prim:  INTEGER           :8978EE9E52AD5DEE313B1401BC04D04FA3F90CA7018FC256AFC67FC200390CBB
    37:d=1  hl=2 l=   3 prim:  INTEGER           :010001

The integers are in hex, so convert it to decimal
    
    n = 0x8978EE9E52AD5DEE313B1401BC04D04FA3F90CA7018FC256AFC67FC200390CBB
    n = 62180528787689937819999198320875604188782593051291064364537897810852251765947

    e = 0x010001
    e = 65537

Now we need to factorize the mod. We do a search at [FactorDB](factordb.com) to help us.
This gives us `p` and `q`
    
    p = 224258454597761606450883324956139951511
    q = 277271726050281009396301232126405463677

To find the private key, we need `d` in addition to `e` and `n`. 
Get `d` by doing `e` mod-inverse `phi` (where `phi = (p-1)(q-1)`)
    
    d = 41901196161721633946390963813492062617560409838048854379776736338651930078713

Finally, we have all the can now construct the private key and this is the result

    -----BEGIN RSA PRIVATE KEY-----
    MIGpAgEAAiEAiXjunlKtXe4xOxQBvATQT6P5DKcBj8JWr8Z/wgA5DLsCAwEAAQIg
    XKM8kT3/i9OOI1SJEq1fvbzsNjcenxVV2DomCFqurfkCEQDQmJeM3hK54QG1GdQs
    pU59AhEAqLabd/WTyoooDc19dX2VlwIQeXiiqDGaDgxthhyoZedNsQIQOPeX3VSV
    t7EYvzhgoXhrNwIQURb6TS79gHK6f+npSDFBPw==
    -----END RSA PRIVATE KEY----- 

The first 32 characters will be the flag: `MIGpAgEAAiEAiXjunlKtXe4xOxQBvATQ`

    

