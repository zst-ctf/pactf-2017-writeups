# Dinosaur Never-forget System (Continued)

### Challenge
> Those Dinosaurs… had money?
> Turns out they also created a ledger system.

### Hint
> I wonder what entry you’re looking for…

### Solution
Referring back to the first challenge, the DNS record is this

    edger entry available at LEDGER subdomain -- flag: dinosaurs_must_stay_informed

This tells us there is a LEDGER subdomain: `LEDGER.dinosaurneverforgetsystem.tk`
Using the same [online DNS record viewer](http://viewdns.info/dnsrecord/), we get this TXT record
    
    3890a940bf54bb50d2ad334d0d0ddbda8a8737b6873277412756724292e89e31

When searching on Google, the first result is this [bitcoin transaction](https://blockchain.info/tx/3890a940bf54bb50d2ad334d0d0ddbda8a8737b6873277412756724292e89e31?show_adv=true). Look at the output scripts and we have our flag
    
    those_dinosaurs_sure_are_clever