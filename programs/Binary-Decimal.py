x=input("binary")
l=len(x)
s=0
for i in range(-1,-l-1,-1):
    s+=int(x[i])*(2**(-i-1))
    
print(s)
