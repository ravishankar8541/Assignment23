#Create a generator to produce squares of first N natural numbers
def f(n):
    x=1
    while n:
        yield x*x
        x+=1
        n-=1
for a in f(9):
    print(a)
