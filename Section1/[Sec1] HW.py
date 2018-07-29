#How to check  a a variable's type ? -> Use type() function, it will return the class of the variable

#Syntax error:
#does not begin with a letter: 21yanny
#contain illegal cahracter: boner$
#contain Python keyword: break

#Circle_area
radius = int(input("What's your radius?"))
circle_area = radius * radius * 3.14
print("its area is " + str(circle_area))

#C_tempt_to_F
tempt = int(input("Enter the temperature in Celsius?"))
new_tempt = tempt * 1.8 + 32
a = "(C)"
print(str(tempt) , a , "=" , str(new_tempt) , "F")

