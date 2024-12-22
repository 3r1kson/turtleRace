from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed("fastest")
def move_forward():
    tim.forward(10)

def change_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def change_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def change_back():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(change_right, "d")
screen.onkey(change_left, "a")
screen.onkey(change_back, "s")
screen.onkey(clear_screen, "c")

screen.exitonclick()
