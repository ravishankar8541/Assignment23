# Create a generator to produce first n even natural numbers

from re import X


def genEVen(n):
    x=2
    while n:
        yield x
        x+=2
        n-=1
for e in genEVen(10):
    print(e,end=" ")      