# 4. Given a dictionary where keys are strings and values are ints,
#  write a program that swaps them so values become keys and keys become values
#   (assuming all values are unique).

dict1 = {
    "rema": 31,
    "suma": 32
}

print(dict1.keys())
print(dict1.values())
dict1 = {value: key for key, value in dict1.items()}
print(dict1)