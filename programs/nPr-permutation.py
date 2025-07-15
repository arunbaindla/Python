def fact(n):
    if n==0 or n==1 :
        return 1 
    elif(n>1):
        return n*fact(n-1)

a=int(input("enter n value in nPr"))
r=int(input("enter r value in nPr"))

print(fact(a)//fact(a-r))
