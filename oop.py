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
#         dog1.name = new_name
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










