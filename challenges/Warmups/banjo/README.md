# Banjo

## Description

<small>Author: @JohnHammond#6971</small><br><br>Oooh, that classic twang! The banjo is one of my favorite  <a href="https://en.wikipedia.org/wiki/Strings_(Unix)"><code>strings</code></a> instruments! <br><br> <b> Download the file below.</b>


## Files

* [banjo.jpg](files/banjo.jpg)

## Solution

The mention of ```string``` indicates that the flag is probably just hidden as plain text inside the provided file.

By running ```strings -n 32 banjo.jpg``` we get back:

```flag{ce4e687e575392ae242f0e41c888de11}```
