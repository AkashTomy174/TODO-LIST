# 3. Write a function that receives a list of numbers and 
# returns the second largest number in the list.

def number():
    a=[]
    print("Enter the limit of numbers")
    n=int(input())
   
    print("Enter the list")
    for i in range(n):
        a.append(int(input()))

    max_num = a[0]
    for i in a:
       if i > max_num:
         max_num = i

    second_max = None
    for i in a:
            if i != max_num:
                if second_max is None or i > second_max:
                    second_max = i

    print(a)
    print(max_num)
    print(second_max)


run=number()


    
  