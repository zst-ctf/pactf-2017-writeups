# MegaEncryption (TM) 

### Challenge
> The Personal Advancement of Cuil Therory Foundation (PACTF) left a message for Tony, but they used MegaEncryption (TM) to encrypt it. What did they say? Should we be worried? It seems like they used some sort of public medium to send the message…

### Hint
> They kept records!

### Solution

I was stuck for so long because I could not find the encrypted message on Wikipedia. Thankfully, some kind soul uploaded it [on pastebin](https://pastebin.com/yq204HEd).

The data is clearly base-64 encoded, and after decrypting it once, another base-64 encoded string was produced. We have to solve it by looping. 

After decoding it for 16 iterations, we get the flag
	
	Oh my goodness! It's gotten so bad. The cuils are rising... they want to outlaw encryption... I'd rate their world +200 Cuils! At least I have MegaEncryption (TM) to keep me safe. the_cuil_is_too_much_to_handle

### Post-challenge
After I solved this, @LFlare told me it can be found [on Wikipedia](https://en.wikipedia.org/w/index.php?title=User_talk:Tony_Tan&oldid=770856430). You must click on "View History" button which I couldn't see because I had a buggy Stylish skin applied :(