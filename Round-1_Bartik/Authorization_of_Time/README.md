# Authorization of Time

### Challenge
> qr.png. `1489798809000`. Get me in.

### Hint
> Big ben just hit `1`.

### Solution
Upon scanning the QR code, I get this 
`otpauth://totp/PACTF%3AMiles?secret=ORUW2ZK7OBQXG43FONPWE5LUL5RXK2LMONPXG5DBPFPXI2DFL5ZWC3LF`.
It seems to be using TOTP. [According to Wikipedia, TOTP is just HOTP with a calculated timestamp value](https://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm#Definition).

    TC = floor((unixtime(now) − unixtime(T0)) / TS)
    TOTP = HOTP(SecretKey, TC)
    
TS is 30 seconds by default, and judging from the scale of the number given in the challenge, it should be in milliseoncds.
We can simplify the formula into this since we can assume what they gave us is ince unix epoch.

    TC = floor(1489798809000 / 30000)
    TOTP = HOTP(SecretKey, TC)

I'll be using the PyOTP library to help me. Since Big ben hit 1, we only need the first value returned.
After inputting all these into a python script, the flag is `808365`
