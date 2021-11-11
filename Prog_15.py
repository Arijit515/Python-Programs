n = int(input("Please enter the start number: "))

m = int(input("Please enter the end number: "))

count = 0
print("prime numbers between", n,"and", m, "are:")
for num in range (n, m+1):
 if num>1:
  for i in range (2,num):
   if num % i==0:
    break
  else: 
    print(num)
    count += 1
print ( "count_prime:", count )