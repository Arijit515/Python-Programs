# Linear Search in Python

lst = []
num = int(input("Enter size of list : "))

for n in range(num):
    numbers = int(input("Enter the array of %d element :" %n))
    lst.append(numbers)

x = int(input("Enter number to search in list :"))

i = 0
flag = False

while i < len(lst):
	if lst[i] == x:
		flag = True
		break

	i = i + 1

if flag == 1:
	print('{} was found at index {}.'.format(x, i))
else:
	print('{} was not found.'.format(x))