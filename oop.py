# class Car:
#     color = 'grey'
#
#     def __init__(self, engine, gearbox):
#         self.engine = engine
#         self.gearbox = gearbox
#
#     def drive(self, km):
#         return f'Машина {self.engine} проехала {km} км'
#
#
# lada = Car(1, 'auto')
# print(lada.drive(100))


# print(lada.__dict__)
# print(bmw.__dict__)
# print(lada.__dict__)

# bmw.color = 'pink'
# print(bmw.__dict__)

# class Person:
#
#     def __init__(self, name, lastname, age=10, gender='male'):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.gender = gender
#
#     def get_year_born(self, current_year):
#         return current_year - self.age
#
#     def get_army(self, current_year):
#         if self.gender == 'male' and and self.age < 18:
#             return f'{self.name} пойдет в армию в {current_year - self.age}'
#
#         return f"{self.name} не годен"
#
#
# vasya = Person('Vasya', 'Ivanov')
# katya = Person('Katya', 'Petrova', age=12)
# print(vasya.get_army(2022))
# print(katya.get_army(2022))


# print(katya.__dict__)
# print(vasya.__dict__)

# 14 1
# class Dog:
#
#     def __init__(self, height, weight, name, age=3):
#
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def jump(self, height):
#         print(f'I can jump {height}m height')
#
#     def run(self, speed):
#         print(f'My speed {speed} km/h')
#
#     def bark(self, say):
#         print(f'I say {say}')
#
#
# bobik = Dog(1, 10, 'Bobik')
# print(bobik.__dict__)
#
# if __name__ == '__main__':
#     bobik.jump(2)
#     bobik.run(15)
#     bobik.bark('bow-wow')

# 14 2
#
# class Dog:
#
#     def __init__(self, height, weight, name, age=3):
#
#         self.height = height
#         self.weight = weight
#         self.name = name
#         self.age = age
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#
# dog1 = Dog(1, 10, 'Bobik')
# print(dog1.name)
#
# if __name__ == '__main__':
#      dog1.change_name('sharik')
#
#
# print(dog1.name)

# *********************
#
# class Building:
#     def __init__(self, floor, windows, doors):
#         self.floor = floor
#         self.windows = windows
#         self.doors = doors
#
#     def build(self):
#         return f'The building was built'
#
#
# class PoliceDepartment(Building):
#     def __init__(self, floor, windows, doors, cars):
#         super().__init__(floor, windows, doors)
#         self.cars = cars
#
#
# police = PoliceDepartment(2, 20, 10, 5)
# police.floor = 3


# class BeautySalonMixin:
#     def salon_opening_hours(self, current_time):
#         if self.salon_close_time >= current_time >= self.salon_open_time:
#             return "Салон работает"
#         return "Салон не работает"
#
#     def set_time_work(self, time_open, time_close):
#         self.salon_open_time = time_open
#         self.salon_close_time = time_close
#
# class HouseWithSalon(Building, BeautySalonMixin):
#     def init(self, floor, windows, doors):
#         super().__init__(floor, windows, doors)
#         self.salon_open_time = None
#         self.salon_close_time = None
#
# house = HouseWithSalon(1, 1, 1)
# house.set_time_work(10, 22)
# print(house.salon_opening_hours(13))
# print(house.salon_opening_hours(23))

# В многоэтажном доме переопределите метод строительства так, чтобы  метод возвращал сколько
# квартир в доме заселено. Не  забудьте, что вы не можете заселить квартир больше, чем вы построили

#
# class Building:
#     def __init__(self, floor, windows, doors):
#         self.floor = floor
#         self.windows = windows
#         self.doors = doors
#
#     def build(self):
#         print(f'The building was built')
#
#     def populate(self):
#         print(f"the house was populated")
#
#
# class MultyStroyHouse(Building):
#     def __init__(self, floor, windows, doors, flats):
#         super().__init__(floor, windows, doors)
#         self.flats = flats
#         self.flats_populated = 0
#
#     def populate(self, flats_to_populate):
#         if flats_to_populate + self.flats_populated <= self.flats:
#             self.flats_populated += flats_to_populate
#         else:
#             print("НЕт столько квартир")


# 14 5 ## 14 6
# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print(f'I can run')
#
#     def jump(self):
#         print(f'.. and jump')
#
#     def birthday(self):
#         print(f'I am {1 + self.age} years old')
#
#     def sleep(self):
#         print(f'I can sleep')
#
#     def __str__(self):
#         print(f'my name is {self.name}')
#         print(f'and my master is {self.master}')
#
#     def portrait(self):
#         self.__str__()
#         self.run()
#         self.jump()
#         self.birthday()
#         self.sleep()
#         if hasattr(self, 'bark'):
#             self.bark()
#         if hasattr(self, 'meow'):
#             self.meow()
#         if hasattr(self, 'fly'):
#             self.fly()
#         print()
#
#
# class Dog(Pet):
#     def bark(self):
#         print(f'..and say bow-wow')
#
#
# class Cat(Pet):
#     def meow(self):
#         print(f'.. and say meow')
#
#
# class Parrot(Pet):
#     def fly(self):
#         print(f'..and can fly')
#
#
# dog1 = Dog('Sharik', 3, 'Vasya')
# cat1 = Cat('Murka', 2, 'Masha')
# parrot1 = Parrot('Ara', 4, 'Lena')
#
# dog1.portrait()
# cat1.portrait()
# parrot1.portrait()
#
# # print(dog1.__str__())
#


# class Building:
#     def init(self, floor, windows, doors, roof):
#         self.floor = floor
#         self.windows = windows
#         self.doors = doors
#         self.__roof = roof
#
#     @property
#     def exit_to_roof(self):
#         return self.__roof
#
#     @exit_to_roof.setter
#     def exit_to_roof(self, value):
#         self.__roof = value
#
#     @exit_to_roof.deleter
#     def exit_to_roof(self):
#         del self.__roof

# class BeautySalonMixin:
#     min_price = 10
#
#     def manicure(self):
#         return BeautySalonMixin.min_price * 1.2
#
#     def haircut(self, hair_length):
#         if hair_length < 30:
#             return BeautySalonMixin.min_price * 1.2
#         elif 30 <= hair_length < 50:
#             return BeautySalonMixin.min_price * 1.5
#         elif 50 <= hair_length:
#             return BeautySalonMixin.min_price * 1.8

# class EmptyString(Exception):
#     def init(self, text):
#         self.text = text


# 14 14 Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
# Добавить валидацию на проверку негативного значения и 0 Используйте дескрипторы
#
# class EmptyString(Exception):
#     def __init__(self, text):
#         self.text = text
#
#
# class Book:
#     def __init__(self, pages, published, price):
#         self.pages = pages
#         self.published = published
#         self.price = price
#         self.author = None
#
#     def set_author(self, name):
#         if name == "":
#             raise EmptyString("Cannot be empty")   # вызвать исключение и текст ошибки
#         self.author = name
#
#
# b = Book(10, 1990, 90)
# b.set_author("")
# print(b.__dict__)
#

#  14 15 Добавьте 14 14 валидацию, чтобы в имени автора не могли  передать пустую строку или число.
# Создайте свой класс  исключения
#
# class NonNegativeZero:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value <= 0:
#             raise ValueError("Cannot be negative")
#         instance.__dict__[self.name] = value
#
#
# class EmptyString(Exception):
#     def __init__(self, text):
#         self.text = text
#
#
# class Book:
#     pages = NonNegativeZero()
#     price = NonNegativeZero()
#     published = NonNegativeZero()
#
#     def __init__(self, pages, published, price):
#         self.pages = pages
#         self.published = published
#         self.price = price
#         self.author = None
#
#     def set_author(self, name):
#         if name == "":
#             raise EmptyString("Cannot be empty")
#         self.author = name

# 14 8 ## 14 9 *********************** домашка *********************
#
#
# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name                    # определяем self name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]  # геттер для self name
#
#     def __set__(self, instance, value):
#         if value <= 0:
#             raise ValueError('cannot be negative or zero')  # вызов текста с ошибкой
#         instance.__dict__[self.name] = value
#
#
# class Pet:
#     age = NonNegative()
#
#     def __init__(self, age, name=None, master=None):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print(f'I can run')
#
#     def jump(self):
#         print(f'.. and jump')
#
#     def birthday(self):
#         print(f'I am {1 + self.age} years old')
#
#     def sleep(self):
#         print(f'I can sleep')
#
#     def __str__(self):
#         if None == self.name or None == self.master:
#             print('!!! I am poor pet, enter my name (master name)!!!!')
#         else:
#             print(f'my name is {self.name}')
#             print(f'and my master is {self.master}')
#
#     def portrait(self):
#         self.__str__()
#         self.run()
#         self.jump()
#         self.birthday()
#         self.sleep()
#         if hasattr(self, 'bark'):
#             self.bark()
#         if hasattr(self, 'meow'):
#             self.meow()
#         if hasattr(self, 'fly'):
#             self.fly()
#         print()
#
#
# class Dog(Pet):
#     def bark(self):
#         print(f'..and say bow-wow')
#
#
# class Cat(Pet):
#     def meow(self):
#         print(f'.. and say meow')
#
#
# class Parrot(Pet):
#     def fly(self):
#         print(f'..and can fly')
#
#
# dog1 = Dog(3, 'Sharik', 'Vasya')
# cat1 = Cat(2)
# parrot1 = Parrot(4, 'Ara', 'Lena')
#
# dog1.portrait()
# cat1.portrait()
# parrot1.portrait()

# ************************** создание класса для собственных исключений *************************
# class MyError(Exception):
#     def __init__(self, text, num):
#         self.txt = text
#         self.n = num
#
#
# a = input("Input positive integer: ")
# try:
#     a = int(a)
#     if a < 0:
#         raise MyError("You give negative!", a)  # текст ошибки
# except ValueError:
#     print("wrong type of value!")
# except MyError:
#     print(MyError)
#     # print(MyError.args)
# else:
#     print(a)

