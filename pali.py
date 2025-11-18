# 2. Given a string, write a program to determine if it is a 
# palindrome (reads the same forwards and backwards).

def reverse(word):
    return word[::-1]

def is_palindrome(word):
    return word == reverse(word)


a = input("Enter the string to check: ")
if is_palindrome(a):
    print("Palindrome")
else:
    print("Not a palindrome")