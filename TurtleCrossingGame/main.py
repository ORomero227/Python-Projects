from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_generator import CarGenerator
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_generator = CarGenerator()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_on = True
while game_on:
    screen.update()
    time.sleep(1.0)

    if player.ycor() > 270:
        player.start_position()
        scoreboard.increment_level()

    for car in car_generator.cars:
        if car.xcor() < -310:
            car.hideturtle()
            car_generator.cars.remove(car)
            car_generator.generate_car()

        if car.distance(player) < -10:
            game_on = False
            scoreboard.game_over()

        car.run()


screen.exitonclick()
