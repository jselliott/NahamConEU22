# Hashstation

## Description

<small>Author: @JohnHammond#6971</small><br><br>Below is a <a href="https://en.wikipedia.org/wiki/SHA-2">SHA256</a> hash! Can you determine what the original data was, before it was hashes? <br><br> <code>705db0603fd5431451dab1171b964b4bd575e2230f40f4c300d70df6e65f5f1c</code> <br><br> <b>Please wrap the original value within the <code>flag{</code> prefix  and <code>}</code> suffix to match the standard flag format.</b>

## Solution

Often with password hashes, you may have to run them through JohnTheRipper or HashCat but in this case it is simple enough that we can just paste it into crackstation.net

This reveals it is a SHA256 hash of the word: "awesome"

```flag{awesome}```