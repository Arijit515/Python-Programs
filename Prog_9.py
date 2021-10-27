a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))


if(a+b+c==180):
    
    if(a<90 and b<90 and c<90):
        print("Acute angled triangle")
        
    elif(a==90 or b==90 or c==90):
        print("Right angled triangle")
        
    else:
        print("Obtuse angled triangle")
    
else:
    print("Not a valid triangle")
 
