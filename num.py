#  Write a function that takes a list of integers and 
# returns a new list containing only the even numbers.

def inputs():
	a=[]
	b=[]
	print("enter the limit of numbers")
	c=int(input())
	print("enter the numbers")
	for i in range(1,c+1):
		a.append(int(input()))
	for num in a:
		if num%2==0:
			b.append(num)
	
	print("entered list",a)
	print("list with even num",b)
			
		
		
result=inputs()


