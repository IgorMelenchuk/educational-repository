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


class Money:

    def __init__(self, money):
        self.money = money

my_money = Money(100)
your_money = Money(1000)


class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
points = list()
for i in range(1, 2001, 2):
    if i == 3:
        points.append(Point(i, i , "yellow"))
        print(points)
    else:
        points.append(Point(i, i))


class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
points = [Point(2*i+1, 2*i+1) for i in range(0, 1000)]
points[1].color = 'yellow'

import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)
class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = [random.choice(random.choices)(random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)) for i in range(217)]
for i in elements:
    if 'Line' in str(i):
        print('find', elements.index(i))
        i.sp = (0, 0)
        i.ep = (0, 0)

