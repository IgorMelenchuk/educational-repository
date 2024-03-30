# Учимся ООП

class Factory:
    pass


class Cat:
    name = 'Матроскин'
    color = 'black'


class Car:
    model = 'BMW'

    def show_ABS(instance):
        if hasattr(instance, 'ABS'):
            print(f'ABS is {instance.ABS}')
        else:
            print('nothing')
    def show_engine(instance):
        if hasattr(instance, 'engine'):
            print(f'Car engine is {instance.engine}')
        else:
            print('nothing')


class Lion:
    name = input(print(f'Введите имя льва'))

    def lion_roar(instance):
        if hasattr(instance, 'name'):
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