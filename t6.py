from turtle import *

speed('fastest')
bgcolor('black')
pencolor('white')
penup()
setpos(-400,100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('red')

penup()
setpos(400,100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('red')

penup()
setpos(-400,-100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('red')

penup()
setpos(400,+100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('red')
    
mainloop()