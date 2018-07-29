print(*range(0, 21))
num = int(input("your number is: "))
print(*range(0, num), sep ="; ")

#my 1 0 sequence
for n in range(10):
    print(1, 0, end=" ")
print(end="\n")

#ur sequence
num10 = int(input("Enter ur number of 1's and 0's: " ))
for i in range(num10):
    if i % 2 == 0:
        print(1, end=" ")
    else:
        print(0, end=" ")



