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

class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024
Goods.price = 2048
setattr(Goods, 'inflation', 100)


class Car:
    pass
setattr(Car,'model','Тойота')
setattr(Car,'color', 'Розовый')
setattr(Car,'number', 'П111УУ77')
print(Car.__dict__['color'])


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2
print(getattr(Notes, 'author'))


class Dictionary:
    rus = "Питон"
    eng = "Python"

print(getattr(Dictionary, 'rus_word', False))

class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()
setattr(tb1, 'name', 'Франция' )
setattr(tb1, 'days', 6 )
TravelBlog.total_blogs += 1

tb2 = TravelBlog()
setattr(tb2, 'name', 'Италия' )
setattr(tb2, 'days', 5 )
name = 'Италия'
days = 5
TravelBlog.total_blogs += 1

class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
fig1.start_pt=(10,5)
fig1.end_pt=(100,20)
fig1.color = 'blue'
if 'color' in fig1.__dict__:
    delattr(fig1, 'color')
print(*fig1.__dict__)

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'
p1 = Person()
if p1.job in p1.__dict__:
    print(True)
else:
    print(False)


class MediaPlayer:
    pass


    def open(self, filename):
        self.filename = filename

    def play(self):
        print(f'Воспроизведение', self.filename)

media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, value):
        self.data = value

    def draw(self):
        filtered_data = [str(num) for num in self.data]
        print(" ".join(filtered_data))
class Stepik:
    def next_task(self):
        return "Следующее задание"


my_st = Stepik()