from rent import Rent


class Service:
    def __init__(self, cars):
        self.cars = cars
        self.rented_cars = []

    def list_free_cars(self):
        print("Free cars:")
        print('\n'.join(
            [str(f"{car.license}, {car.brand} {car.model} Consumption: {car.lp100} l/100,"
                 f"Price per hour: {car.cost_per_hour}$ "
                 f"Price per day: {car.cost_per_day}$ Price per week: {car.cost_per_week}$")
              for car in self.cars if car not in self.rented_cars]
        ), '\n')

    def rent(self, rentals, client):
        if isinstance(rentals, Rent):
            rentals = [rentals]

        free_cars = self.get_free_cars(rentals)
        if free_cars:
            total_cost = self.get_total(rentals, free_cars)
            print("Successfully rented car(s):", '\n', '\n'.join(map(str, free_cars)))
            print(f"Total cost: {total_cost}")
            client.add_cars(*free_cars, total_cost)
            self.rented_cars.extend(free_cars)

    def get_free_cars(self, rentals):
        free_cars_list = []
        for car_id in [rental.car_license for rental in rentals]:
            car = next((car for car in self.cars if car.license == car_id), None)
            if not car:
                print(f"{car_id}:there is no such card")
                return

            if car in self.rented_cars:
                print(f"{car_id} has been rented already!")

                continue


            free_cars_list.append(car)

        return free_cars_list

    @staticmethod
    def get_total(rentals, free_cars_list):
        total = 0

        for car in free_cars_list:
            rental = next(rental for rental in rentals if rental.car_license == car.license)
            total += (rental.hours * car.cost_per_hour) + \
                     (rental.days * car.cost_per_day) + \
                     (rental.weeks * car.cost_per_week)

        return total
