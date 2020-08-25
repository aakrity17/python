# Write a Python function to sum all the numbers in a list. 

li=[2,1,3,4]
x=0
for i in li:
	x=x+i
print(x)

#using function

def sum(numbers):
	su=0
	for i in numbers:
		su=su+i
	return su
print(sum((3,1,2,4)))
