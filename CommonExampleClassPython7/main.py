# class AlwaysNounsNotVerbs:
#     """сlass documentation comment
#     опис класу: що він робить, для чого призначений
#     """
#
#     # 1. класові (статичні) змінні - належать класу, спільні для всіх екземплярів
#     class_counter = 0
#     DEFAULT_TIMEOUT = 30
#
#     def __init__(self, name: str, value: int = 0):
#         """конструктор (метод ініціалізації екземпляра)"""
#         # 2. екземплярні змінні (instance variables)
#         self.name = name  # self.__dict__["name"] = name
#         self.value = value
#         self._internal_state = None  # приватна (за домовленістю) змінна екземпляра класу
#
#         # збільшуємо лічильник створених об'єктів
#         AlwaysNounsNotVerbs.class_counter += 1
#
#     # 3. звичайні методи екземпляра
#     def do_something(self, param: str) -> str:
#         """один з основних методів класу"""
#         return f"{self.name} зробив {param}"
#
#     # 4. статичний метод (не потребує self), логічно належить класу,
#     # але не має доступу ні до стану екземплярів, ні до стану класу
#     # це просто функція, яка організаційно належить класу (наприклад, для утилітарних цілей), але не використовує його стан
#     @staticmethod  # https://www.designgurus.io/answers/detail/what-is-the-difference-between-staticmethod-and-classmethod-in-python
#     def get_version() -> str:
#         return "1.0.4"
#
#     # одна з ключових відмінностей Python від багатьох інших мов:
#     # !!! класи — це повноцінні об'єкти з власним станом.
#     # кожен клас — це об'єкт (конкретний екземпляр свого метакласу, зазвичай type).
#     # цей об'єкт-клас:
#     # - існує один на весь клас (не створюється заново при кожному створенні екземпляра)
#     # - тримає стан класу (те, що спільне для всіх екземплярів)
#     # - цей стан живе саме в цьому об'єкті-класі
#
#     # 5. метод класу (отримує клас як перший аргумент)
#     # це надбудова, якої бракує в C++/Java/C#, яка дозволяє:
#     # - писати зручні альтернативні конструктори
#     # - працювати з підкласами поліморфно
#     # - змінювати стан класу без створення екземпляра
#     @classmethod  # це вже більше схоже на статичний метод, але він отримує клас як перший аргумент (cls), що дозволяє йому працювати з класом і його підкласами
#     def from_default(
#             cls) -> 'AlwaysNounsNotVerbs':  # cls - це посилання на клас, який викликав цей метод (може бути підкласом)
#         return cls(
#             "DefaultObject")  # тут повертається новий екземпляр класу, створений за допомогою конструктора __init__
#
#     # 6. протектед метод (за конвенцією з _ на початку), для приватного - __ на початку, і так само це буде лише домовленість
#     def _update_internal(self):
#         self._internal_state = "updated"
#
#
# #####################################################################################
#
# if __name__ == "__main__":
#     obj1 = AlwaysNounsNotVerbs("Sensor-01", 42)
#     obj2 = AlwaysNounsNotVerbs.from_default()
#
#     print(obj1.do_something("перевірку"))
#     print(AlwaysNounsNotVerbs.get_version())
#     print(f"Створено об'єктів: {AlwaysNounsNotVerbs.class_counter}")
#
# #####################################################################################
# # знизу ще приклад :)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def print_info(self):
#         print("Student name: " + self.name)
#
#
# s = Student("John")
# s.print_info()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Student:
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print("Student name: " + self.name + ", Age: " + str(self.age))
#
#
# s = Student("John", 18)
# s.print_info()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Student:
#     def __init__(self, name: str):
#         self.__name = name
#
#
# s = Student("Alex")
# print(s.__name)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

#як зробити статичне поле (статичний атрибут)

# class Student:
#     def __init__(self, name: str):
#         self.__name = name
#
#
# s = Student("Alex")
# print(s._Student__name)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class AlwaysNounsNotVerbs:
#     # 1. класові (статичні) змінні — можна позначити явно як ClassVar
#     class_counter: ClassVar[int] = 0
#     DEFAULT_TIMEOUT: ClassVar[int] = 30

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# ТИПОВИЙ КЛАСС:

# from dataclasses import dataclass, field
# from datetime import date
# from enum import Enum
# from random import randint
# from typing import List, ClassVar
#
#
# class EyesColor(Enum):
#     YELLOW = "Yellow"
#     BLACK = "Black"
#     BROWN = "Brown"
#     GREEN = "Green"
#     BLUE = "Blue"
#     DIFFERENT = "Different"
#     BLIND = "Blind"
#
#
# @dataclass  # @dataclass за замовчуванням додає такі методи: __init__ __repr__ __eq__ (і відповідно __ne__)
# # залежно від параметрів декоратора додаються ще:
# # order=True (__lt__, __le__, __gt__, __ge__)
# # frozen=True (__hash__)
# # https://www.it-notes.wiki/python/what-is-dataclasses/
# # https://docs.python.org/3/library/dataclasses.html
# # https://habr.com/ru/articles/415829/
# class Cat:
#     # виглядають як статичні, але це екземплярні поля КЛАСУ (з типами та значеннями за замовчуванням)
#     gender: int = 0
#     nick: str = ""
#     craziness: int = 0
#     hungry: int = 50
#     color: str = ""
#     paws: int = 4
#     lives: int = 9
#     has_tail: bool = True
#     has_fur: bool = True
#     eyes_color: EyesColor = EyesColor.GREEN
#     birthdate: date = field(default_factory=lambda: date(2026, 1, 1))
#     favourite_meal: List[str] = field(default_factory=lambda: ["Whiskas", "Milk"])
#     weight: float = 5000.0  # грами
#     kind: str = ""
#     energy: int = 100
#     is_alive: bool = True
#
#     # приклад статичних полів
#     SPECIES: ClassVar[str] = "Felis catus"
#     total_cats: ClassVar[int] = 0
#
#     # @dataclass автоматично згенерує конструктор __init__, але його можна перевизначити, якщо потрібно
#     # згенерується щось на кшталт цього:
#     # def __init__(self,
#     #     # ось звідки візьмуться атрибути для майбутніх об'єктів
#     #     gender: int = 0,
#     #     nick: str = "",
#     #     craziness: int = 0,
#     #     hungry: int = 50,
#     #     color: str = "",
#     #     paws: int = 4,
#     #     lives: int = 9,
#     #     has_tail: bool = True,
#     #     has_fur: bool = True,
#     #     eyes_color: EyesColor = EyesColor.GREEN,
#     #     birthdate: date = None,
#     #     favourite_meal: List[str] = None,
#     #     weight: float = 5000.0,
#     #     kind: str = "",
#     #     energy: int = 100,
#     #     is_alive: bool = True,
#     # ) -> None:
#     #     self.gender = gender
#     #     self.nick = nick
#     #     self.craziness = craziness
#     #     self.hungry = hungry
#     #     self.color = color
#     #     self.paws = paws
#     #     self.lives = lives
#     #     self.has_tail = has_tail
#     #     self.has_fur = has_fur
#     #     self.eyes_color = eyes_color
#
#     #     if birthdate is None:
#     #         self.birthdate = date(2026, 1, 1)
#     #     else:
#     #         self.birthdate = birthdate
#
#     #     if favourite_meal is None:
#     #         self.favourite_meal = ["Whiskas", "Milk"]
#     #     else:
#     #         self.favourite_meal = favourite_meal
#
#     #     self.weight = weight
#     #     self.kind = kind
#     #     self.energy = energy
#     #     self.is_alive = is_alive
#
#     # методи
#     def play(self) -> None:
#         if self.paws <= 0:
#             print("В котика нема лапок, він не може гратися!")
#             return
#         if self.hungry == 100:
#             print("Кіт голодний!")
#             return
#         if self.energy < 20:
#             print("Кіт втомився...")
#             return
#         if not self.is_alive:
#             print("Котик помер :(")
#             return
#
#         self.energy -= 10
#         self.craziness += randint(-5, 5)
#         self.hungry += randint(0, 10)
#         self.weight -= randint(0, 1000)
#
#     def sleep(self) -> None:
#         self.hungry = 100
#         self.energy = 100
#
#     def eat(self, meal: str) -> None:
#         if meal in self.favourite_meal:
#             self.hungry = 0
#             self.energy = 100
#             self.craziness -= 10
#             self.weight += 1000
#             self.make_sound()
#             return
#
#         # не улюблена їжа
#         self.hungry -= 10
#         self.energy += 10
#
#     def make_sound(self) -> None:
#         print("Няв-няв!")
#
#     def print_info(self) -> None:
#         print("================================")
#         print(f"Кличка:       {self.nick}")
#         print(f"Характер:     {self.craziness}")
#         print(f"Голодний:     {self.hungry}")
#         print(f"Лапки:        {self.paws}")
#         print(f"Життів:       {self.lives}")
#         print(f"Вага:         {self.weight:.0f}g")
#         print(f"Егенрійність: {self.energy}")
#         print("================================")
#
#     def set_paws(self, value: int) -> None:
#         if value < 0 or value > 4:
#             value = 4
#         self.paws = value
#
#
# #############################################################################
#
# if __name__ == "__main__":
#     cat1 = Cat(nick="Локі", hungry=30, craziness=15)
#     cat1.gender = 1
#     cat1.print_info()
#
#     cat1.play()
#     cat1.eat("Whiskas")
#     cat1.print_info()
#
#     cat2 = Cat(nick="Фрея", hungry=40, craziness=20)
#     cat2.gender = 0
#     cat2.print_info()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

#звичайні екземплярні поля!!!

# @dataclass
# class Cat:
#     gender: int = 0
#     nick: str = ""
#     craziness: int = 0
#     hungry: int = 50
#     color: str = ""

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from dataclasses import dataclass
#
#
# @dataclass
# class Dog:
#     name: str
#     age: int
#     paws: int
#
#
# d = Dog("Sharik", 2, 4)
# print(d.name)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# __str__
# __eq__
# __ne__
#
# __hash__
# __repr__

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# # entities / Cat.py
#
# from dataclasses import dataclass
#
# @dataclass
# class Cat:
#     name: str
#     age: int = 2
#     height: float = 0.5
#     weight: float= 5
#
#     def display(self):
#         print(self.name, self.age, self.height, self.weight)
#
#
# def test():
#     print("test")
#
#
# x = 100

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# main.py

# from entities.Cat import Cat
#
# c = Cat("Barsik")
# c.display()
# print(c.name)
# print(c.age)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from entities.Cat import *

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# __all__ = ["Cat", "test", "x"]

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# __all__ = ["Cat"]
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Cat:
#     name: str = "Barsyk"
#     age: int = 2

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from entities.Cat import *
#
# c = Cat()
# c.age = 3.4
#
# print(c.age)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Cat:
#     def __init__(self, weight):
#         self.__weight = weight # прихований атрибут
#     # замість явних геттерів та сеттерів
#     @property # використовуються властивості
#     def weight(self):
#         # геттер
#         return self.__weight
#     @weight.setter
#     def weight(self, value):
#     # сеттер
#         if value > 0:
#             self.__weight = value
#         else:
#             print("Вага має бути більше нуля")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# __all__ = ["Cat"]
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Cat:
#     name: str = "Barsyk"
#     __age: int = 2  # зробити поле приватним !!!
#
#     @property
#     def age(self) -> int:
#         return self.__age
#
#     @age.setter
#     def age(self, age) -> None:
#         if type(age) != int:
#             raise TypeError("Cat age value must be an integer type")
#
#         if age <= 0 or age > 39:
#             raise ValueError("Cat age must be between 0 and 39")
#
#         self.__age = age

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from entities.Cat import *
#
# c = Cat()
# c.age = -100
#
# print(c.age)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////













from geometry.rectangle import Rectangle

if __name__ == "__main__":
    rect = Rectangle(5.5, 3.2)

    print(f"Початкова ширина: {rect.width}")
    print(f"Початкова висота: {rect.height}")
    print(f"Площа: {rect.get_area()}")
    print(f"Периметр: {rect.get_perimeter()}")

    print("-" * 30)

    rect.width = 10.0
    rect.height = 4.5

    print(f"Нова ширина: {rect.width}")
    print(f"Нова висота: {rect.height}")
    print(f"Нова площа: {rect.get_area()}")
    print(f"Новий периметр: {rect.get_perimeter()}")








