class Customer:
    def __init__(self, name):
        self.name = name
        self.money = []
        self.cars = []

    def add_cars(self, cars, money):
        self.cars.append(cars)
        self.money.append(money)
