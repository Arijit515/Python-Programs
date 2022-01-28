def gcd(x, y):
    while(y):
       x, y = y, x % y
    return x
def lcm(x, y):
    lcm = (x*y)//gcd(x,y)
    return lcm
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:")) 
print("The L.C.M. is", lcm(num1, num2))
print("GCD of two numbers is ",gcd(num1,num2))