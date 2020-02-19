# Variables, lists and function

print("Hello World!")

# variables are single items, with different types, like integer, float, string, boolean

value = 500
print(value)
# list are groups of items, where you can point to one of the items, numbers start with 0

fruits = ("apple", "banana", "orange")
print(fruits)
print(fruits[2])
print("\n")

# functions are block with a specific action

def print_all(items):
    count = 0
    for item in items:
        print(items[count])
        count += 1


print_all(fruits)
