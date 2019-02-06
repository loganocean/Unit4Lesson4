from turtle import *

screen = Screen()
screen.bgcolor("turquoise")

bob = Turtle()

bob.color("blue")
bob.pensize(2)
bob.speed(5)
bob.shape("turtle")

for x in range(1000):
	bob.forward(150)
	bob.left(15)
	bob.backward(150)
	bob.left(10)

mainloop()