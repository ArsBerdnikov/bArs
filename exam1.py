# 1 1 С клавиатуры вводится 7мизначное число. Если четных цифр в нем
# больше, чем нечетных, то найти сумму всех цифр. Если нечетных больше, чем
# четных, то найти произведение 1, 3 и 6 цифр.

# num = int(input('enter number: '))
# odd = 0
# even = 0
# total = 0
# while num > 0:
#     last_num = num % 10
#     total = last_num + total
#     if last_num % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     num = num // 10
# if even > odd:
#     print(f'четных больше, сумма {total}')
# elif odd > even:
#     print(int(num[0]) * int(num[2]) * int(num[5]))

# 1 2 С клавиатуры вводится строка. Если количество согласных и гласных в ней одинаково, то
# выведите на экран все гласные буквы

# vowels = 'aeiouy'
# count_vow = 0
# count_2 = 0
# word = input('enter word: ').lower()
# vowels_list = []
# for i in word:
#     if i in vowels and i.isalpha:
#         count_vow += 1
#         vowels_list.append(i)
#     else:
#         count_2 += 1
# if count_vow == count_2:
#     print(vowels_list)

# 1 3 С клавиатуры вводятся 2 числа a и b и генеруется 2 числа рандомно r1 и r2. Все числа от 1 до 20.
# Посчитать сколько раз a > r1 and b > r2. Проверку выполнить 6 раз. В случае равенства (когда a, b больше 3 раза и r1,
# r2 больше 3 раза) вывести на печать рандомные числа полученные в 4 итерации.
# import random

# a_more_r1 = 0
# b_more_r2 = 0
# iter = 1
# random_list = []
# while iter <= 6:
#     a = int(input('enter number: '))
#     b = int(input('enter number: '))
#     r1 = random.randint(1, 20)
#     r2 = random.randint(1, 20)
#     if a > r1:
#         a_more_r1 += 1
#     elif b > r2:
#         b_more_r2 += 1
#     iter += 1
#     if iter == 4:
#         random_list.append(r1)
#         random_list.append(r2)
# print(a_more_r1)
# print(b_more_r2)
# if (a_more_r1 + b_more_r2) == 3:
#     print(random_list)

# 1 4
# import random

# goal = int(input('какую цифру ищем: '))
# c = int(input('сколько раз ищем: '))
# iter = 1
# count = 0
# while iter <= c:
#     num = random.randint(1, 20)
#     while num != 0:
#         last = num % 10
#         if last == goal:
#             count += 1
#         num = num // 10
#     iter += 1
# print(f'{goal} встречается {count} раз')

# 1 5

# numbers = '1234567890'
# text = input('enter text: ')
# for i in text:
#     if i in numbers:
#         print(i)

# 1 6

# text = input()
# pair_upper = 0
# pair_lower = 0
# vowels_count = 0
# cons_count = 0
# numbers = '1234567890'
# vowels = 'aeiouyAEIOUY'
# symbols = '-=+*/<>'

# for i in range(1, len(text)):
#     if text[i].isalpha and text[i-1].isalpha:
#         if text[i-1].isupper() and text[i].isupper():  #-1 чтобы начало считать с 0, т.к. range считает  с 1
#             pair_upper += 1
#         if text[i-1].islower() and text[i].islower():
#             pair_lower += 1

# for i in text:
#     if i.isalpha and i in vowels:
#         vowels_count += 1
#     else:
#         cons_count += 1
# print(f'парных букв в верхнем регистре {pair_upper}')
# print(f'парных букв в нижнем регистре {pair_lower}')
# print(f'гласных букв {vowels_count}')
# print(f'согласных букв {cons_count}')
# print(f'всего букв ({cons_count} + {vowels_count})')

