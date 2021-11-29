#Write a Python program to remove duplicates from an integer list(Elements supplied by the user). Find 2nd largest number from the list.
list = []  
num_list = int(input("Enter number of elements in list: "))
 
for i in range(1, num_list + 1):  
    element = int(input("Enter the elements: "))  
    list.append(element)  
list.sort()  
print("Second largest element is:", list[-2])

