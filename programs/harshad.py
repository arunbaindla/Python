harshad--- number is divisible by sum of its digits ex: 18/(1+9) 
n=int(input(" enter teh number "))
s=0
for j in str(n):
    s=s+int(j)
    
if n%s==0:
    print(f"{n} is a hasrhad number ")
-------------------------------------------------------------
harshad number in given range 
def har(n):
    s=0
    for j in str(n):
        s=s+int(j)
        
    if n%s==0:
        print(n,end=" ")
    
for i in range(1,101):
    har(i)
