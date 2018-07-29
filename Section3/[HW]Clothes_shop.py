line = "Welcome to our shop, what do you want (C, R, U, D)?"
a = "Our items: "
items = ["T-shirt", "Sweater"]
for i in range(4):
    deci = input(line)
    if deci == "C":
        items.append(input("Enter new item: "))
        print("{0}{1}".format(a, items))
    elif deci == "R":
        print(("{0}{1}".format(a, items)))
    elif deci == "U":
        items[int(input("Update postion? ")) - 1] = input("New item ?")
        print(print("{0}{1}".format(a, items)))
    elif deci == "D":
        items.pop(int(input("Delete position? ")))
        print(print("{0}{1}".format(a, items)))
