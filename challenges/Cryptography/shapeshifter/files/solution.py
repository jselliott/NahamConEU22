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