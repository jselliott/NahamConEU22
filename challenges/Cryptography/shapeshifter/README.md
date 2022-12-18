# Shapeshifter

## Description

<small>Author: @Gary#4657</small><br><br>These bits are shapepshifting! I need some help getting them back to their original form.  Someone told me this might be a  <a href="https://en.wikipedia.org/wiki/Linear-feedback_shift_register#Fibonacci_LFSRs"><code>Fibonacci LFSR</code></a>.  <br><br> <b>Download the files below.</b>


## Files

* [output.txt](files/output.txt)

* [shapeshifter.py](files/shapeshifter.py)

## Solution

For this challenge we are given a python file that reads in the file and performs some mathematical operations and outputs a strange list of binary characters in the output file.

```python
from Crypto.Util.number import bytes_to_long as b2l

FLAG = open('flag.txt', 'r').read().strip().encode()

class LFSR():
    def __init__(self, iv):
        self.state = [int(c) for c in iv]
        #self.state = self.iv

    def shift(self):
        s = self.state
        newbit = s[15] ^ s[13] ^ s[12] ^ s[10] # ^ s[0]
        s.pop()
        self.state = [newbit] + s

for i in range(0, len(FLAG), 2):
    chars = f'{b2l(FLAG[i:i+2]):016b}'
    assert len(chars) == 16

    lfsr = LFSR(chars)
    for _ in range(31337):
        lfsr.shift()

    finalstate = ''.join([str(c) for c in lfsr.state])
    print(f'{finalstate}')



```

Looking at the code, we can see that the flag is converted, two characters at a time, into binary (so 16 bits). 
Next, the LSFR class is initialized with the binary characters and the shift() function is called on each one 31337 times. Then, the final output from the shifted input it printed.

Examining the code for the shift function, we can see that it essentially shifts all the bits to the right while adding a new bit onto the front of the list that is the XOR of bits 15,13,12, and 10.

```python
newbit = s[15] ^ s[13] ^ s[12] ^ s[10]
```

The index is important here because it means that if we wanted to reverse the process, then we know that the old final bit must be equal to:

```python
oldbit = s[0] ^ s[14] ^ s[13] ^ s[11]
```

Because the only thing we really lost was the last bit in the shift right, the opposite of that is taking the shifted bits and XORing them with the first one while shifting left instead.

My solution script below uses the function shift() which takes an input and a number of shifts to perform. So if we tell it to shift everything 31337 times back in the opposite direction, then we are given back the original flag.

```python
from Crypto.Util.number import bytes_to_long as b2l

def shift(x,n):
    for i in range(n):
        x = x[1:] + [x[0] ^ x[11] ^ x[13] ^ x[14]]
    return x

with open("output.txt") as F:
    for line in F.readlines():
        bits = [int(b) for b in line.strip()]
        X = "".join([str(x) for x in shift(bits,31337)])
        c1 = chr(int(X[:8],2))
        c2 = chr(int(X[8:],2))
        print(c1+c2,end="")
```

**Flag: flag{70f817ce030904aa1db980686ffa0fa8}** 
