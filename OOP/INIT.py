class Cat:


    def __init__(self, name, breed='pers', age=1, color='black'):
        print('Hello new object is', self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

class Laptop:

    def __init__(self, brand, model, price):
        print('Hello new object is', self, brand, model, price)
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{brand} {model}'


class SoccerPlayer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f"{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}")


class Zebra:
    def __init__(self):
        self.stripe_color = "white"

    def which_stripe(self):
        if self.stripe_color == "white":
            print("Полоска белая")
            self.stripe_color = "black"
        else:
            print("Полоска черная")
            self.stripe_color = "white"


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        print(f'{self.last_name} {self.first_name}')


    def is_adult(self):
        if self.age >= 18:
            print(True)
        else:
            print(False)
