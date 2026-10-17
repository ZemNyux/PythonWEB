# /////////////////////////////////////////////////////////////////////////////

# print("hello")
# name = "Alex" # str
# age = 354738576564738287436584736857648756283476582374658746584765837465837465873648576348756837456837465873645345345347856354354234543453483454326 # int
# address = 'Ukraine' # str
# growth = 1.77 # float
# hasGitHub = True # bool
# print(name)
# print(age)

# print(name + " " + str(age))
# print(f"Name: {name}, Age: {age}")

# /////////////////////////////////////////////////////////////////////////////

# PI = 3.1415926 # const final absent
# print(PI)
# PI = 4
# print(PI)

# /////////////////////////////////////////////////////////////////////////////

# name = input("Enter your name: ")
# print("Hello, " + name)

# /////////////////////////////////////////////////////////////////////////////

# age = input("Enter your age: ") # "36"
# print(int(age) + 1)

# /////////////////////////////////////////////////////////////////////////////

# age = 25
# age = "Alex"
# print(age)

# /////////////////////////////////////////////////////////////////////////////

# a = 10
# b = 4
# print(a / b) # 2.5
# print(a // b) # 2
# print(a / 0)

# /////////////////////////////////////////////////////////////////////////////

# try:
#     print(10 / 0)
# except:
#     print("Some error occured")

# /////////////////////////////////////////////////////////////////////////////

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("ZeroDivisionError occured")
# print("NEXT INSTRUCTION")

# /////////////////////////////////////////////////////////////////////////////

# # && || !
# # and or not

# warmToday = True
# isRainToday = False

# if not warmToday: # !warmToday
#     print("Cold Today")

# /////////////////////////////////////////////////////////////////////////////

# # && || !
# # and or not

# warmToday = True
# isRainToday = False

# if warmToday and not isRainToday:
#     print("WALK")
# else:
#     print("SIT AT HOME")

# /////////////////////////////////////////////////////////////////////////////

# growth = 1.77

# match growth:
#     case x if x > 2.00:
#         print("basketball")
#     case x if x <= 2.00:
#         print("tankist")

# /////////////////////////////////////////////////////////////////////////////

# from unittest import case

# day = 4

# match day:
#     case 1:
#         print("monday")
#     case 2:
#         print("tuesday")
#     case 3:
#         print("wednesday")
#     case 4:
#         print("thursday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturday")
#     case 7:
#         print("sunday")
#     case _:
#         print("some another day")

# /////////////////////////////////////////////////////////////////////////////

# import random

# number = random.randint(-10, 100)
# print(number)

# /////////////////////////////////////////////////////////////////////////////

# import random

# number = random.uniform(-10, 100)
# print(number)

# number = random.randint(-10, 100)
# print(number)

# number = random.random()
# print(number)

# /////////////////////////////////////////////////////////////////////////////

# import random

# days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# print(random.choice(days))
# print(days[random.randint(0, len(days) - 1)])

# number = random.uniform(-10, 100)
# print(number)

# number = random.randint(-10, 100)
# print(number)

# number = random.random()
# print(number)

# /////////////////////////////////////////////////////////////////////////////

# start = 0
# end = 10
# current = start
# while current <= end:
#     print(current)
#     current += 1

# /////////////////////////////////////////////////////////////////////////////

# start = 0
# end = 10
# current = start
# while current <= end:
#     print(current, end=", ")
#     current += 1

# /////////////////////////////////////////////////////////////////////////////

# for i in range(1, 10): print(i, end=" ")

# /////////////////////////////////////////////////////////////////////////////

# for i in range(1, 11, 3):
#     print(i, end=" ") # 1 4 7 10

# /////////////////////////////////////////////////////////////////////////////

# for i in range(11):
#     print(i, end=" ")

# /////////////////////////////////////////////////////////////////////////////

# for i in range(11, 1, -3):
#     print(i, end=" ")

# /////////////////////////////////////////////////////////////////////////////

# for y in range(height):
# for x in range(width):
# # виводимо зірочку, якщо ми на межі або в першому/останньому ряду
# if y == 0 or y == height 1 or x == 0 or x == width 1:
# print("@", end="")
# else:
# print(".", end="")
# print() #
# перехід на новий рядок після кожного ряду
# input()

# /////////////////////////////////////////////////////////////////////////////

# user_input = input("Please enter login: ")
# login = "admin"

# if user_input.lower() == login.lower():
#     print("Login successful")
# else:
#     print("Login failed")

# /////////////////////////////////////////////////////////////////////////////

# login = "admin"
# print(login[0]) # a
# login[0] = 'X' # error !!!

# /////////////////////////////////////////////////////////////////////////////

# login = "admin"
# print(login[0]) # a
# login = login.replace('a', 'X')
# print(login) # Xdmin

# /////////////////////////////////////////////////////////////////////////////

# import string

# text = input("введите строку: ")

# text = text.lower()

# cleaned_text = ""
# for char in text:
#     if char not in string.punctuation and char != " ":
#         cleaned_text += char

# if cleaned_text == cleaned_text[::-1]:
#     print("строка является палиндромом")
# else:
#     print("строка не является палиндромом")

# /////////////////////////////////////////////////////////////////////////////

# ar = [1, 2, 3, 3.1415, 2.6434, "Alex", "admin", [1,2,3], True, (1,2,3)]
# print(ar)

# print(ar[0])

# ar[0] = 10
# print(ar)

# ar.append(123)
# print(ar)

# /////////////////////////////////////////////////////////////////////////////

# even_numbers = [x for x in range(1, 51) if x % 2 == 0]
# print("Парні числа від 1 до 50:", even_numbers, "\n\n")

# /////////////////////////////////////////////////////////////////////////////

# fruits = ["яблуко", "банан", "вишня", "груша"]
# indexed_values = [f"Індекс {i}: {value}" for i, value in enumerate(fruits)]
# print("Комбінація індексу та значення:", indexed_values)

# //////////////////////////////////

# def function():
#     print("Hello World")
#     print("My name is Nikita")

# function()
# function()

# /////////////////////////////////////////////////////////////////////////////

# def function():
#     print("Hello World")
#     print("My name is Nikita")

# def function(x):
#         print(x)

# function()
# function()

# /////////////////////////////////////////////////////////////////////////////

# def function(a:int=0, b:int=0, c:int=0) -> int:
# result = a + b + c
# return result

# print(function(1,2,3))

# /////////////////////////////////////////////////////////////////////////////

# x = 10

# def test(a):
#     a = 20

# test(x) # змінні передаються за значенням!
# print(x) # 10

# /////////////////////////////////////////////////////////////////////////////

# x = [10, 20, 30, 40]

# def test(a):
#     a.append(50) # елемент додається в оригінальний список

# test(x) # посилання на список ТЕЖ передаються за значенням (копіюється)
# print(x) # 

# /////////////////////////////////////////////////////////////////////////////

# def function(a:int=0, b:int=0, c:int=0) -> int:
#     result = a + b + c
#     return result

# print(function(b=50, c=30, a=10))

# /////////////////////////////////////////////////////////////////////////////

# f_open
# open("path", "a+")

# file = open("C:/Users/Nikita/Desktop/hello.txt", "a+", encoding="utf8")

# text = input("Введіть рядок: ")
# file.write(text)
# file.close()
 

# /////////////////////////////////////////////////////////////////////////////

# import os

# for i in range(1, 11): # тут можна змінити кількість файлів
#     # формуємо шлях до файлу
#     path = f"C:\\1\\{i}.txt"
    
#     # виводимо шлях на екран
#     print(path)
    
#     try:
#         # відкриваємо файл для запису
#         with open(path, "w") as f:
#             f.write("Привіт!") # записуємо рядок у файл
            
#         # os.remove(path) # якщо потрібно видалити файл
#         # os.makedirs(path, exist_ok=True) # створення папки
#         # os.rmdir(path) # видалення папки
#     except Exception as e:
#         print(f"сталася помилка при роботі з файлом {path}: {e}")

# /////////////////////////////////////////////////////////////////////////////

# import os

# os.makedirs(r"C:\Users\nikit\Desktop\MyFolder", exist_ok=True)

# for i in range(1, 10001):
#     path = f"C:\\Users\\nikit\\Desktop\\MyFolder\\{i}.txt"

#     print(path)

#     try:
#         with open(path, "w") as f:
#             f.write("Python")
#     except Exception as e:
#         print(f"сталася помилка при роботі з файлом {path}: {e}")

# /////////////////////////////////////////////////////////////////////////////

# import os
# import shutil

# # шлях до папки
# path = r"C:\Users\nikit\Desktop\PythonFiles"

# try:
#     # видаляємо папку разом з усіма файлами
#     shutil.rmtree(path)
#     print("Папку видалено!")
# except Exception as e:
#     print(f"сталася помилка: {e}")

# /////////////////////////////////////////////////////////////////////////////



# /////////////////////////////////////////////////////////////////////////////



# /////////////////////////////////////////////////////////////////////////////



# /////////////////////////////////////////////////////////////////////////////