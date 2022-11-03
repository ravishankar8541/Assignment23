"""Create an endless iterator using generator method to produce terms of Fibonacci
series"""

def fab():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
it=fab()
fib_lsit=[]
while True:
    bag=input("Do you want to generate another element[y/n]") 
    if bag=='y':
        x=next(it)
        print(x)
        fib_lsit.append(x)
    else:
        break
print(fib_lsit)    


