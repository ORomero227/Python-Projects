import random
from car import Car


class CarGenerator:
    def __init__(self):
        self.cars = []
        self.generate_first_cars()

    def generate_first_cars(self):
        for _ in range(15):
            self.generate_car()

    def generate_car(self):
        new_car = Car()
        random_x = random.randint(310, 350)
        random_y = random.randint(-230, 260)
        new_car.goto(x=random_x, y=random_y)
        self.cars.append(new_car)

    def increase_move_speed(self):
        for car in self.cars:
            car.move_speed *= 2
