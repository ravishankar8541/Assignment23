#Create a generator to produce first n prime numbers
def fun(n):
    i=2
    while i<=n:
        count=0
        for a in range(2,(i//2)+1):
            if i%a==0:
                count+=1
        if count==0:
            yield i 
        i+=1           
for r in fun(30):
    print(r,end=" ")        

