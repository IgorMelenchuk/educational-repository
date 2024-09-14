# Получаем количество минут от пользователя
minutes = int(input())

# Вычисляем количество часов и остаток минут
hours = minutes // 60
remainder_minutes = minutes % 60

# Выводим результат
print(f"{minutes} мин - это {hours} час {remainder_minutes} минут.")


#Проверка пароля
a = int(input('Введите пароль:'))
b = int(input('Еще раз введите пароль:'))
if a==b:
    print('Пароль верный')
else:
    print('Пароль неверный')


#Проверка на четность
a = int(input('Введите число'))
if a / 2 or a // 2:
    print('Число четное')
else:
    print('Число нечетное')


#Проверяем возраст
a = int(input('Для регистрации введите ваш возраст:'))
if a >= 18:
    print('Доступ разрешен')
else:
    print('Доступ запрещен')

#являются ли три заданных числа (в указанном порядке) последовательными членами арифметической прогрессии
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
if b - a == c - b:
    print("YES")
else:
    print("NO")


#Наименьшее из двух
a = int(input('Введите число:'))
b = int(input('Введите число:'))
print(min(a, b))


#Наименьшее из четырех
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
d = int(input('Введите число:'))
print('Наименьшее число:', min(a, b, c, d))

#Определяем зрезость
age = int(input('Введите ваш возраст'))
if age >= 13:
    print('Детство')
elif age >= 24:
    print('Молодость')
elif age >= 59:
    print('Зрелость')
else:
    print('Старость')

#Подсчет суммы положительных чисел
a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))
sum_positive = max(0,a) + max(0, b) + max(0, c)
print(sum_positive)


#Принадлежность промежутку
a = int(input(''))
if -1<a and a<17:
    print('Принадлежит')
else:
    print('Не принадлежит')

#Принадлежность промежутку
a = int(input())
if not(-3 < a < 7):
    print('Принадлежит')
else :
    print('Не принадлежит')

#Принадлежность промежутку
a = int(input())
if not(-30 and -3 <= a <= 25):
    print('Принадлежит')
else :
    print('Не принадлежит')

#Красивое ли число
number = int(input())

if 1000 <= number <= 9999 and (number % 7 == 0 or number % 17 == 0):
    print("YES")
else:
    print("NO")

#Невырожденный треугольник
a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")

#высокостный год
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("YES")
else:
    print("NO")


#Ход ладьи
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == c or b == d:
    print("YES")
else:
    print("NO")

#Нахождение совпадающих
a, b, c = int(input()), int(input()), int(input())

if a == b:
    if b == c:
        print(3)
    else:
        print(2)
else:
    if a == c:
        print(2)
    else:
        if b == c:
            print(2)
        else:
            print(0)
#Или так
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)

#Или вот так
a, b, c = int(input()), int(input()), int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

#Гонка
n = 'Зум'
k = 'Flash'
n, k = int(input()), int(input())
if n > k:
    print('NO')
elif k > n:
    print('YES')
elif n == k:
    print("Don't know")

#Вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a and b and c > 0 and a==b==c:
    print('Равносторонний')
elif a == b or b==c or a==c:
    print('Равнобедренный')
else:
    print('Разносторонний')

#Серединное число
a = int(input())
b = int(input())
c = int(input())

middle_value = a + b + c - max(a, b, c) - min(a, b, c)

print(middle_value)

#Количество дней
month = int(input())

if month == 2:
    days = 28
elif month in [4, 6, 9, 11]:
    days = 30
else:
    days = 31

print(days)

#Считываем вес
# Считываем вес боксера
weight = int(input())

# Определяем весовую категорию
if weight < 60:
    print('Легкий вес')
elif weight < 64:
    print('Первый полусредний вес')
elif weight < 69:
    print('Полусредний вес')

#Чтение трех целых чисел
a, b, c = map(int, input().split())
print(a, b, c)

#Чтение производного количества целых чисел
lst_int = list(map(int, input().split()))
print(lst_int)

type = 5


# Вместимость автобуса
import math

# Ввод значений n и m
n, m = map(int, input().split())

# Суммируем количество детей и вожатых
total_people = n + m

# Вычисляем минимальное количество автобусов, округляя вверх
buses_needed = math.ceil(total_people / 20)

# Вывод результата на экран
print(buses_needed)


