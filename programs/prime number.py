Check if the number is prime or not 
------------------------------------------------
 n=int(input("enter a number : "))
count=0
for i in range(2,n):
    if(n%i==0):
        count=count+1
if(count>=1):
    print("not prime ", n)
else:
    print("prime")

----------------------------------------------------------
Prime numbers in the given range 

num=int(input("enter numbers till large"))
st=int(input("enter minimum limit"))
for j in range(st,num+1):
    count=0
    for i in range(1,j+1):
        if(j%i==0):
            count=count+1
    if(count==2):
        print(i)

-----------------------------------------------------------
prime num using functions 

	def prime(n):
	    count=0
	    for i in range(2,n):
	        if(n%i==0):
	            count=count+1
	    if(count==0 and n>2):
	        return "is prime"
	    else:
	        return "not prime"
	        
print(prime(10))

------------------------------------------------------
Prime factors

n=int(input("enter num "))
c=0
for i in range (1,n+1):
    if(n%i==0):
        for j in range(2,i):
            if(i%j==0):
                c=c+1
        if(c==0):
            print(i)
