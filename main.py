import json

from car import Car
from customer import Customer
from rent import Rent
from service import Service


def one():
    print(f"Ok {dummy_customer.name}, Here is the list of the available cars!")
    service.list_free_cars()
    print(f"Which car do you want ro rent?(Type in the license plate)")
    license = input()
    print(f"For how long?")
    print(f"hours :")
    hours = int(input())
    print(f"days :")
    days = int(input())
    print(f"weeks")
    weeks = int(input())
    dummy_rent = Rent(license, hours=hours, days=days, weeks=weeks)
    service.rent(dummy_rent, dummy_customer)


def two():
    print("Final Order:\n")
    get_customer_info(dummy_customer)

    exit()


def three():
    service.list_free_cars()


def four():
    get_customer_info(dummy_customer)


def get_customer_info(customer):
    if len(customer.cars) > 2:
        to_pay = sum(customer.money) * 0.7
        round(to_pay, 2)
        string = f"You get additional discount of 30 % and the total is {to_pay}"
    else:
        to_pay = sum(customer.money)
        round(to_pay, 2)
        string = f"The total is {to_pay}"
    print(f"{customer.name} has rented {len(customer.cars)} cars.")
    print(*customer.cars, sep='\n')
    print(string)


with open('db.json') as cars_db:
    cars = json.load(cars_db)

service = Service([Car.from_dict(car) for car in cars])

print(f"Register new client.")
print(f"Please type in your name!")

dummy_customer = Customer(input())
print(f"Ok {dummy_customer.name}, Here is the list of the available cars!")
service.list_free_cars()
print(f"Which car do you want ro rent?(Type in the license plate)")
license = input()
print(f"For how long?")
print(f"hours :")
hours = int(input())
print(f"days :")
days = int(input())
print(f"weeks")
weeks = int(input())

dummy_rent = Rent(license, hours=hours, days=days, weeks=weeks)
service.rent(dummy_rent, dummy_customer)

while 1:
    print(
        f"If you want to add more cars press 1 "
        f"\nIf you want to finish press 2 "
        f"\nIf you want to see the available cars press 3"
        f"\nIf you want to see summary press 4")
    choice = int(input())
    if choice == 1:
        one()
    elif choice == 2:
        two()
    elif choice == 3:
        three()
    elif choice == 4:
        four()
