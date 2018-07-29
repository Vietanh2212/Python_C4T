sizes = [6, 8, 300, 100, 69, 128, 752]
print("Hello, my name is Viet Anh and these are my ship sizes:", sizes, sep="\n")
print("Now my biggest ship has size", max(sizes), "let's shear it")
sizes[sizes.index(max(sizes))] = 8
print("after shearing, here is my flock", sizes, sep="\n")
for months in range(int(input("How much months u want to travel to? ")) + 1 ):
    for num in range(len(sizes)):
        sizes[num] += 50
    print("MONTH " + str(months) + ":", "One month has passed, now here is my flock", sizes, sep="\n")
    print()
su = str(sum(sizes)); cash = sum(sizes) * 2
print("My flock has size in total: " + su, "I would get " + su + "* 2$ = " + str(cash) + "$", sep="\n")
