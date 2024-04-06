# Учимся ООП

class Factory:
    pass


class Cat:
    name = 'Матроскин'
    color = 'black'


class Car:
    model = 'BMW'

    def show_ABS(self):
        if hasattr(self, 'ABS'):
            print(f'ABS is {self.ABS}')
        else:
            print('nothing')
    def show_engine(self):
        if hasattr(self, 'engine'):
            print(f'Car engine is {self.engine}')
        else:
            print('nothing')

    def show_price(self):
        if hasattr(self, 'price'):
            print(f'Car price is {self.price}')
        else:
            print('nothing')



    def set_price(self,value,age='New'):
        self.price = value
        self.age = value

    def set_engine(self,value):
        self.engine = value


class Lion:
    name = input(print(f'Введите имя льва'))

    def lion_roar(self):
        if hasattr(self, 'name'):
            print(f'Rrrrrr!!!')
        else: print(f'Неопознанный лев')


class Counter:
    def __init__(self):
        self.value = 0

    def start_from(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def display(self):
        print(f"Текущее значение счетчика = {self.value}")

    def reset(self):
        self.value = 0

