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
class Pet:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'I can run')

    def jump(self):
        print(f'.. and jump')

    def birthday(self):
        print(f'I am {1 + self.age} years old')

    def sleep(self):
        print(f'I can sleep')

    def __str__(self):
        print(f'my name is {self.name}')
        print(f'and my master is {self.master}')

    def portrait(self):
        self.__str__()
        self.run()
        self.jump()
        self.birthday()
        self.sleep()
        if hasattr(self, 'bark'):
            self.bark()
        if hasattr(self, 'meow'):
            self.meow()
        if hasattr(self, 'fly'):
            self.fly()
        print()


class Dog(Pet):
    def bark(self):
        print(f'..and say bow-wow')


class Cat(Pet):
    def meow(self):
        print(f'.. and say meow')


class Parrot(Pet):
    def fly(self):
        print(f'..and can fly')


dog1 = Dog('Sharik', 3, 'Vasya')
cat1 = Cat('Murka', 2, 'Masha')
parrot1 = Parrot('Ara', 4, 'Lena')

dog1.portrait()
cat1.portrait()
parrot1.portrait()

# print(dog1.__str__())

