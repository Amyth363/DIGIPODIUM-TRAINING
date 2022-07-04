from turtle import *

speed('fastest')
bgcolor('black')
pencolor('orange')
penup()
setpos(-100,100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(-300,100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(100,-100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')

penup()
setpos(300,-100)
pendown()
for i in range(200,0,-3):
    forward(i)
    left(90)
    pencolor('white')


mainloop()

