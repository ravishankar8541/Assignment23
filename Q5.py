#Create a generator to produce first n terms of Fibonacci series
def f1(n):
    a,b=0,1
    while n:
        yield a
        a,b=b,a+b
        n-=1
for a in f1(8):
    print(a,end=" ")
