#my table
print("I have this table:", end="\n")
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print(end="\n")

#your table
ezreal = int(input("Choose the side of ur table: "))
for lux in range(1, ezreal + 1):
    for akali in range(1, ezreal + 1):
        print(lux * akali, end=" ")
    print(end="\n")
