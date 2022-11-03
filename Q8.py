#Create an endless iterator using generator method to produce Prime numbers
def fun():
    i=2
    while True:
        count=0
        for a in range(2,(i//2)+1):
            if i%a==0:
                count+=1
        if count==0:
            yield i 
        i+=1           
it=fun()   
fib_list=[]
while True:
    ans=input("Do you want to generate another element[y/n]")
    if ans=='y':
        x=next(it) 
        print(x)
        fib_list.append(x)
    else:
        break
print(fib_list)        
