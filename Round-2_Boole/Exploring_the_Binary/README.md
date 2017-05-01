# Exploring the Binary!!! 

### Challenge
> Binary 1
> Why doesn’t [this](a.3cd409c8df9a.out) file print!! Did I forget to put in the print statement when I compiled?

### Hint
> Well running it does nothing, maybe try looking inside?

### Solution
We can use `xxd` in Unix to see the contents inside.
After doing so, searching for flag in the output gives us this the answer `flag_1297831859`