# Hometask_13_6 Напишите функцию, вычисляющую значение факториала числа N.

# def fact(x):
#     if x == 1:
#         return 1
#     return fact(x-1)*x
#
#
# print(fact(int(input('enter number: '))))


# Hometask_13_5
#
# cake = {"наполеон": ["масло, мука, сахар", 7, 1100],
#         "медовик": ["мука, сахар, мед", 15, 1200],
#         "киевский": ["мука, сливки, крем", 10, 1500]}
#
#
# def descript():
#     print(f'Торт {cake_type} состоит из {cake[cake_type][0]}')
#
#
# def price():
#     print(f'Цена торта {cake_type} {cake[cake_type][1]} рублей')
#
#
# def quantity():
#     print(f'Торт {cake_type} осталось {cake[cake_type][2]} грамм')
#
#
# def buy():
#     weight = int(input("Сколько торта Вам положить: "))
#     print(f'к оплате {cake[cake_type][1] * weight / 100}')
#     print(f'торта {cake_type} осталось {cake[cake_type][2] - weight}')
#
#
# def not_available():
#     print(f'торта {cake_type} нет')
#
#
# cake_type = input("Какой торт Вы хотели бы приобрести: ").lower()
#
# if cake_type not in cake:
#     not_available()
# else:
#     cake_wish = input("Что Вы хотели бы уточнить: ").lower()
#     if cake_wish == "описание":
#         descript()
#     elif cake_wish == "цена":
#         price()
#     elif cake_wish == "количество":
#         quantity()
#     elif cake_wish == "купить":
#         buy()
#
# print('Спасибо, Желаете чего-то еще?')

# 13 4
# import random
#
#
# def rand_list(a, b, c):
#     for i in range(a):
#         random_list.append(random.randint(b, c))
#     return random_list
#
#
# random_list = []
# print(rand_list(7, 2, 12))
