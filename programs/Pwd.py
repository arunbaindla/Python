To check if the password satisfies all conditions :

def ppp(n):
    a,b,p,z=0,0,0,0
    spl=["$",'#','@']
    for c in n:
        if c.isupper() :
            a+=1
        elif c.isdigit():
            b+=1 
        elif c in spl:
            z+=1
        elif c.islower():
            p+=1
    if(len(n)>6 and len(n)<13 and a>=1 and b>=1 and z>=1 and p>=1):
        print("password accepted :", n)
    else:
        print("Password conditions not satisfied ")

n=input("enter pwds ").split(",")
for w in n:
    ppp(w)
    
