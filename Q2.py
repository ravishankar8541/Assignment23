#Create a generator to produce first n odd natural numbers

from re import X


def genOdd(n):
    x=1
    while n:
        yield x
        x+=2
        n-=1
for e in genOdd(10):
    print(e,end=" ")        