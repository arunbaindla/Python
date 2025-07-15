def fact(n):
    if n==0 or n==1 :
        return 1 
    elif(n>1):
        return n*fact(n-1)

a=int(input("enter n value in nCr"))
r=int(input("enter r value in nCr"))

print(fact(a)//(fact(r)*fact(a-r)))
