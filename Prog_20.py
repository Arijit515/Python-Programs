n = int(input("Enter the number of rows"))
for i in range(n,0,-2):
    for j in range(i,n+1,2):
        print(j,end="")
    print()