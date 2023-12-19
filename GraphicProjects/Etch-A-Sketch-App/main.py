from turtle import Turtle, Screen

jack = Turtle()
screen = Screen()


def move_forwards():
    jack.forward(10)


def move_backwards():
    jack.backward(10)


def move_counter_clockwise():
    jack.left(10)


def move_clockwise():
    jack.right(10)


def clear():
    jack.clear()
    jack.penup()
    jack.home()
    jack.pendown()


screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.listen()
screen.exitonclick()
