height = int(input("give me ur height (cm): "))
mass = int(input("give me ur mass (kg): "))
bmi = mass / (height * height) * 10000
print(bmi)
a = "your conditon is"
if bmi < 16:
    print(a, "severly underweight")
elif bmi < 18.5:
    print(a, "underweight")
elif bmi <= 25:
    print(a, "normal")
elif bmi <= 30:
    print(a, "overweight")
else:
    print(a, "obese")



