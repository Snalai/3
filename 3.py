# 1. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите два варианта решения: через list и через dict.
# Пример:
# Введите номер месяца: 10
# Результат через список: Осень
# Результат через словарь: Осень
# """
# """

# LMonths = ["зима", "весна", "лето", "осень"]
# print("Введите целое число от 1 до 12")
# n = int(input())
# if n > 0 and n < 13:
#     if n < 3 or n == 12:
#         print(LMonths[0])
#     elif n > 2 and n < 6:
#         print(LMonths[1])
#     elif n > 5 and n < 9:
#         print(LMonths[2])
#     elif n > 8 and n < 12:
#         print(LMonths[3])
# else:
#     print("Введите целое число от 1 до 12!!!")


# DMonths = {'12': 'зима', '1': 'зима', '2': 'зима', '3': 'весна', '4': 'весна', '5': 'весна',
#            '6': 'лето', '7': 'лето', '8': 'лето', '9': 'осень', '10': 'осень', '11': 'осень'}
# print("Введите целое число от 1 до 12")
# print(DMonths[input()])

# 2. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль (try except).

# Пример:
# Введите первое число: 10
# Введите второе число: 0
# Вы что? Пытаетесь делить на 0!

# Process finished with exit code 0

# Пример:
# Введите первое число: 10
# Введите второе число: 10
# 1.0
# Process finished with exit code 0
# """
# """
# print("Введите первое число:")
# firsrtNumber = int(input())
# print("Введите второе число:")
# SecondNumber = int(input())
# if SecondNumber != 0:
#     result = firsrtNumber/SecondNumber
#     print(result)
# else:
#     print("Вы что? Пытаетесь делить на 0!")


# 3. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

# Пример:
# Иван Иванов 1846 года рождения, проживает в городе Москва,
# email: jackie@gmail.com, телефон: 01005321456
# """
# """
# print(f"{input('Введите ваше имя: ')} {input('Введите вашe Фамилию: ')} {input('Введите ваш год рождения: ')} года рождения, проживает в городе {input('Введите ваш город проживания: ')}, \nemail: {input('Введите ваш email: ')}, телефон: {input('Введите ваш номер телефона: ')}")


# def status(name, surname, age, city, email, num):
#     print(f"{name} {surname} {age} года рождения, проживает в городе {city}, \nemail: {email}, телефон: {num}")


# status(input('Введите ваше имя: '), input('Введите вашe Фамилию: '), input('Введите ваш год рождения: '), input(
#     'Введите ваш город проживания: '), input('Введите ваш email: '), input('Введите ваш номер телефона: '))


# 4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
# Попробуйте решить задачу двумя способами:
# 1) используя функцию sort()
# 2) без функции sort()
# """

# 1)
# def my_func(a, b, c):
#     f = sorted([a, b, c])
#     return print(f[-1]+ f[-2])
# my_func(int(input()),int(input()),int(input()))

# 2)
# def my_func(a, b, c):
#     if a > b and a > c:
#         if b > c:
#             return print(a + b)
#         else:
#             return print(a + c)
#     elif b > a and b > c:
#         if a > c:
#             return print(a + b)
#         else:
#             return print(b + c)
#     elif a > b:
#         return print(a + c)
#     else:
#         return print(b + c)
# my_func(int(input()), int(input()), int(input()))

# ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ:
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# N = int(input())
# a = [i for i in range(1, N)]
# X = int(input())
# print(a.count(X))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
# N = int(input())
# a = [i for i in range(1, N)]
# X = int(input())
# if True == (X in a):
#     print(X)
# elif N < X:
#     print(N)
# else:
#     print(a[0])
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
#  А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#  Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*
# ноутбук
#     12

# У меня с помощью upper() никак не получилось сразу преобразовывать в верхний регистр поэтому он работает если писать только в верхнем регистре

# Scrabble = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': '1', 'N': 1, 'S': 1, 'T': 1, 'R': 1, 
#             'D': 2, 'G': 2,
#             'B': 3, 'C': 3, 'M': 3, 'P': 3, 
#             'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 
#             'K': 5, 
#             'J': 8, 'X': 8, 
#             'Q': 10, 'Z': 10, 
#             'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#             'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#             'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#             'Й': 4, 'Ы': 4,
#             'Ж': 15, 'З': 15, 'Х': 15, 'Ц': 15, 'Ч': 15,
#             'Ш': 8, 'Э': 8, 'Ю': 8,
#             'Ф': 10, 'Щ': 10, 'Ъ': 10}

# Word = input()

# sum = 0
# for i in Word:
#     c = int(Scrabble.get(i))
#     sum = sum + c
# print(sum)
