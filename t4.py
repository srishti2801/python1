from turtle import *

speed('slowest')
pencolor('red')

sides = 15
for i in range(sides):
    forward(75)
    left(360/sides)
    dot(30)

mainloop()