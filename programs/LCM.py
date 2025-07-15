a=int(input("a"))
b=int(input(" b "))

def gcd(a,b):
    n=1
    if(a>b and a%b==0):
        return b
    elif(b>a and b%a==0):
        return a
    elif(a>b):
        for i in range(2,b+1):
            if(a%i==0 and b%i==0):
                n=n*i
        return n
    else:
        for l in range(2,a+1):
            if(a%l==0 and b%l==0):
                n=n*l
        return n
        
def lcm(a,b):
    z=0
    z=(a*b)//gcd(a,b) 
    return z

print(lcm(a,b))

------------------------------------------------------

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Function to find the GCD using the Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Euclidean algorithm step
    return a

# Function to find the LCM
def lcm(a, b):
    return (a * b) // gcd(a, b)  # Using the LCM formula

# Output the LCM
print("LCM of", a, "and", b, "is:", lcm(a, b))

