# 1_1 Дан список.Выведите те его элементы, которые встречаются в списке только один раз.
# ls = input().split()
# for i in ls:
#     if ls.count(i) == 1:
#         print(i)

# 2_2 Дан список символов. Посчитайте сколько в нем пар элементов, равных друг другу
# (одинаковых). Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# ls = input().split()
# s = set(ls)
# print(len(ls) - len(s))

# 3_1 Дано два кортежа. Определите сумму элементов какого из кортежей больше и выведите
# соответсвующее сообщение в формате: «Сумма больше в кортеже …
# t1 = tuple(int(i) for i in input().split())
# t2 = tuple(int(i) for i in input().split())
# if sum(t1) > sum(t2):
#     print(f"Сумма больше в кортеже {t1}")
# elif sum(t2) > sum(t1):
#     print(f"Сумма больше в кортеже {t2}")


# 3_2 Дан кортеж. Вывести на экран порядковый номер максимального элемент
# n = tuple(int(i) for i in input().split())
# # d = max(n)
# print(n.index(max(n)))

# 4_1 Дана строка. Создайте из нее словарь, где ключами будут символы, а значением
# количество его появлений в строке
# data = input()
# # d = {}
# # for i in data:
# #     d[i] = data.count(i)
# d = {i: data.count(i) for i in data}
# print(d)

# 5_1Клиент приходит в пиццерию. Реализуйте менб, чтобы клиент мог посмотреть описание и цену:
# 1. Если клиент захочет посмотреть описание, выведите название пиццы и из чего она состоит
# 2. Если клиент захочет посмотреть цену, выведить «пицца … стоит … рублей»
# В качестве меню создайте словарь: ключ – пицца, значение – описание, цена за 100 грамм.

# pizza = {"неаполитана": ["тесто, вода, соль", 7],
#               "мясная": ["тесто, колбаса, курица", 12]}
#
# kind_pizza = input("Какая пицца интересует: ").lower()
# wish = input("Что хотели бы уточнить: ").lower()
#
# if wish == "описание":
#     print(f'состав: {pizza[kind_pizza][0]}')
# elif wish == "цена":
#     print(f'пицца {kind_pizza} стоит {pizza[kind_pizza][1]} рублей')
# else:
#     print("такого нет")


# 5_2 Клиент выбрал пиццу. Реализуйте заказ клиента. Клиент вводит какую пиццу он хочет купить
# и сколько грамм. Программа выводит стоимость покупки и сколько пиццы осталось в пиццерии в граммах.

# pizza = {"неаполитана": ["тесто, вода, соль", 7, 876],
#               "мясная": ["колбаса, курица", 12, 1012]}
#
# kind_pizza = input("Какая пицца интересует: ").lower()
# gr = int(input("Сколько пиццы положить: "))
#
# print(f"к оплате {pizza[kind_pizza][1] * gr / 100}")
# print(f"пиццы {kind_pizza} осталось {pizza[kind_pizza][-1] - gr}"


# 6_1 Даны два списка чисел, некоротые элементы их одинаковы
# Посчитайте, сколько уникальных элементов содержится только в первом списке
#
# ls_1 = [int(i) for i in input().split()]
# ls_2 = [int(i) for i in input().split()]
# c = 0
# for i in ls_1:
#     if i not in ls_2:
#         c += 1
# print(c)

# 8_1 В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка больше 4 баллов
# with open('111.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip("\n")
#         mark = int(line[-1])
#         if mark > 4:
#             print(line)

# 8_2 В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран сумму всех оценок

# scores = 0
# with open('111.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip("\n")
#         mark = int(line[-1])
#         scores += mark
# print(f'Сумма всех оценок = {scores}')

# 8_3 В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Посчитать сколько оценок всего

# c = 0
# with open('111.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip("\n")
#         c += 1
# print(f'Всего {c} оценок')
# a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
# a[2] = []
# print(a)
# c = tuple(b)
# print(type(c))
#
# a_dict = {'foo': 100, 'bar': 200, 'baz': 300}
# d_items = a_dict.items()
# print(d_items)

# ################################################################
# # 2 1
# lst = input().split()
# for i in lst:
#     if lst.count(i) == 1:
#         print(i)

# 2 2
# lst = input().split()
# s = set(lst)
# print(len(lst) - len(s))

# 2 3
# c1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
# c2 = (45, 21, 124, 76, 5, 23, 91, 234)
# if sum(c1) > sum(c2):
#     print(f"Сумма больше в кортеже {c1}")
# elif sum(c2) > sum(c1):
#     print(f"Сумма больше в кортеже {c2}")
# print(f'В кортеже с1 минимальный элемент {min(c1)}, максимальный элемент {max(c1)}')
# print(f'В кортеже с2 минимальный элемент {min(c2)}, максимальный элемент {max(c2)}')

# 2 4
# data = ' An apple a day keeps the doctor away'
# d = {i: data.count(i) for i in data}
# print(d)

# # 2 5
import pyttsx3

engine = pyttsx3.init()  # инициализация движка
# зададим свойства
engine.setProperty('rate', 200)  # скорость речи
engine.setProperty('volume', 0.9)  # громкость

cake = {"наполеон": ["масло, мука, сахар", 7, 1100],
        "медовик": ["мука, сахар, мед", 15, 1200],
        "киевский": ["мука, сливки, крем", 10, 1500]}

engine.say("Какой торт Вы хотели бы приобрести")
engine.runAndWait()
cake_type = input("Какой торт Вы хотели бы приобрести: ").lower()
if cake_type not in cake:
    print(f'торта {cake_type} нет')
    engine.say(f'торта {cake_type} нет')
    engine.runAndWait()
else:
    engine.say("Что Вы хотели бы уточнить")
    engine.runAndWait()
    cake_wish = input("Что Вы хотели бы уточнить: ").lower()
    if cake_wish == "описание":
        print(f'Торт {cake_type} состоит из {cake[cake_type][0]}')
        engine.say(f'Торт {cake_type} состоит из {cake[cake_type][0]}')
        engine.runAndWait()
    elif cake_wish == "цена":
        print(f'Цена торта {cake_type} {cake[cake_type][1]} рублей')
        engine.say(f'Цена торта {cake_type} {cake[cake_type][1]} рублей')
        engine.runAndWait()
    elif cake_wish == "количество":
        print(f'Торт {cake_type} осталось {cake[cake_type][2]} грамм')
        engine.say(f'Торт {cake_type} осталось {cake[cake_type][2]} грамм')
        engine.runAndWait()
    elif cake_wish == "купить":
        engine.say("Сколько торта Вам положить")
        engine.runAndWait()
        weight = int(input("Сколько торта Вам положить: "))
        print(f'к оплате {cake[cake_type][1] * weight / 100}')
        print(f'торта {cake_type} осталось {cake[cake_type][2] - weight}')
print('Спасибо, Желаете чего-то еще?')
engine.say('Спасибо, Желаете чего-то еще?')
engine.runAndWait()


# 2 6
# ls_1 = [int(i) for i in input().split()]
# ls_2 = [int(i) for i in input().split()]
# st1 = set(ls_1)
# st2 = set(ls_2)
# print(len(st1 & st2))

# 2 7
# lst = []
# try:
#     file = open('text3.txt', 'w')
#     text = file.read()
# except FileNotFoundError:
#     print('нужно создать файл с данными')
# else:
#     print(text)
# finally:
#     file.close()

# 2 8
# marks = []
# with open('111.txt', 'r') as f:
#     for line in f:
#         line = line.rstrip("\n")
#         mark = int(line[-1])
#         marks.append(mark)
#         if mark < 3:
#             print(line)
# print(f'Средняя оценка за тест = {sum(marks) / len(marks)}')
# print(marks)
# print(len(marks))

# import pyttsx3
# engine = pyttsx3.init() # инициализация движка
# # зададим свойства
# engine.setProperty('rate', 150) #скорость речи
# engine.setProperty('volume', 0.9) #громкость
# engine.say("Какой торт")
# engine.runAndWait()


# import pyttsx3
#
# tts = pyttsx3.init()
#
# voices = tts.getProperty('voices')
#
# # Задать голос по умолчанию
# tts.setProperty('voice', 'ru')
#
# # Попробовать установить предпочтительный голос
# for voice in voices:
#     if voice.name == 'Aleksandr':
#         tts.setProperty('voice', voice.id)
#
# tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
# tts.runAndWait()
