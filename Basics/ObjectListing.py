# a function to list all given object

names = list()
datas = list()
objects = list()
while True:
    choice = input("Want to make a new object? y/n ")
    if choice == "y":
        names.append(input("What is the object's name? "))
        datas.append(float(input("What is the object's number? ")))
    elif choice == "n":
        break
    else:
        print("You must answer with y or n")
        continue

# print(names)
# print(datas)

def increase_list(database, names, datas):
    num = 0
    for name in names:
        database.append({name, datas[num]})
        num += 1

increase_list(objects,names,datas)
print(objects)