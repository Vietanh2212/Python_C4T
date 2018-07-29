a = int(input(("số a ")))
b = int(input(("số b ")))
c = int(input(("số c ")))

delta = b*b - 4*a*c
delta_sqrt = delta ** 0.5
if delta < 0:
    print("no variable")
else:
    print("giá trị X1 là: " + str((-b + delta_sqrt)/(a + a)))
    print("giá trị X2 là: " + str((-b - delta_sqrt)/(a + a)))


    