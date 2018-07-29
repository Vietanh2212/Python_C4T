#1
import turtle
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
angle = [3, 4, 5, 6, 7]
scr = turtle.Screen()
naruto = turtle.Turtle()
naruto.shape('turtle')
naruto.speed(5)
naruto.pensize(0)
for co, an in zip(colors, angle):
    naruto.color(co)
    for i in range(an):
        i += 1
        naruto.forward(100)
        naruto.left(360 / an)

naruto.reset()

#2
for i in range(5):
    naruto.begin_fill()
    naruto.color('white', colors[i])
    for loop in range(2):
        naruto.forward(25)
        naruto.left(90)
        naruto.forward(50)
        naruto.left(90)
    naruto. forward(25)
    naruto.end_fill()


scr.mainloop()
