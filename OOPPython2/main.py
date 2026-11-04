# from typing import Self
#
#
# class Vector2D:
#     """
#     2D-вектор з "магічними" методами,
#     ці методи роблять клас зручним і "pythonic"
#     """
#
#     def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
#         self.x = x
#         self.y = y
#
#     # ─────────────────────────────────────────────────────────────
#     # 1. представлення об'єкта (дуже часто використовується)
#     # ─────────────────────────────────────────────────────────────
#     def __repr__(self) -> str:
#         """Для розробників: однозначне відтворення об'єкта.
#         Те, що повернеться, можна скопіювати з консолі, або повідомлення телеграм,
#         а потім можна виконати як код і отримати ідентичний об’єкт.
#         Порада: завжди робити repr - це must-have для будь-якого класу"""
#         return f"Vector2D({self.x!r}, {self.y!r})"
#
#     def __str__(self) -> str:
#         """Для користувачів: гарне текстове представлення"""
#         return f"({self.x:.2f}, {self.y:.2f})"
#
#     # ─────────────────────────────────────────────────────────────
#     # 2. порівняння (дуже часто потрібно)
#     # ─────────────────────────────────────────────────────────────
#     def __eq__(self, other: object) -> bool:
#         if not isinstance(other, Vector2D):
#             return NotImplemented
#         return self.x == other.x and self.y == other.y
#
#     def __lt__(self, other: Self) -> bool:
#         """Для сортування, min/max тощо"""
#         if not isinstance(other, Vector2D):
#             return NotImplemented
#         return (self.x ** 2 + self.y ** 2) < (other.x ** 2 + other.y ** 2)
#
#     # ───────────────────────────────────────────────
#     # 3. арифметика (один з найпопулярніших наборів)
#     # ───────────────────────────────────────────────
#     def __add__(self, other: Self) -> Self:
#         if not isinstance(other, Vector2D):
#             return NotImplemented
#         return Vector2D(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other: Self) -> Self:
#         if not isinstance(other, Vector2D):
#             return NotImplemented
#         return Vector2D(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, scalar: float | int) -> Self:
#         """Підтримка множення на число: v * 3"""
#         if not isinstance(scalar, (int, float)):
#             return NotImplemented
#         return Vector2D(self.x * scalar, self.y * scalar)
#
#     def __rmul__(self, scalar: float | int) -> Self:
#         """Підтримка зворотного множення: 3 * v"""
#         return self.__mul__(scalar)
#
#     def __neg__(self) -> Self:
#         return Vector2D(-self.x, -self.y)
#
#     # ───────────────────────────────────────────────
#     # 4. довжина та bool-значення
#     # ───────────────────────────────────────────────
#     def __abs__(self) -> float:
#         """abs(v) > довжина вектора"""
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#     def __bool__(self) -> bool:
#         """if v: ... > чи ненульовий вектор"""
#         return self.x != 0 or self.y != 0
#
#     # ───────────────────────────────────────────────
#     # 5. доступ по індексу (дуже зручно)
#     # ───────────────────────────────────────────────
#     def __getitem__(self, index: int) -> float:
#         if index == 0:
#             return self.x
#         if index == 1:
#             return self.y
#         raise IndexError("Vector2D має лише два компоненти: 0 > x, 1 > y")
#
#     def __len__(self) -> int:
#         return 2
#
#     # ──────────────────────────────────────────────────────────────────────────
#     # 6. контекст-менеджер (опціонально, але корисно)
#     # завдяки цим двом методам клас може використовуватися в конструкції with
#     # ──────────────────────────────────────────────────────────────────────────
#     def __enter__(self) -> Self:
#         print("Вектор увійшов у контекст")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
#         print("Вектор вийшов з контексту")
#
#     # ─────────────────────────────────────────────────────────────
#     # 7. хешування (якщо планується використання в set/dict)
#     # ─────────────────────────────────────────────────────────────
#     def __hash__(self) -> int:
#         return hash((self.x, self.y))
#
#     # повтор для hash+eq !!!
#     # технічно не обов’язковий, можна залишити тільки один екземпляр __eq__
#     # вище в класі, але більшість досвідчених розробників вважають за краще
#     # дублювати (або принаймні коментувати), бо це покращує читабельність,
#     # зменшує ймовірність помилок при рефакторингу та робить код самодокументованим
#     def __eq__(self, other: object) -> bool:
#         if not isinstance(other, Vector2D):
#             return NotImplemented
#         return self.x == other.x and self.y == other.y
#
#
# ########################################################################################
#
# if __name__ == "__main__":
#     v1 = Vector2D(3, 4)
#     v2 = Vector2D(1, 2)
#
#     print(v1)  # (3.00, 4.00)
#     print(repr(v1))  # Vector2D(3.0, 4.0)
#     print(v1 + v2)  # (4.00, 6.00)
#     print(v1 * 2)  # (6.00, 8.00)
#     print(3 * v1)  # (9.00, 12.00)
#     print(-v1)  # (-3.00, -4.00)
#     print(abs(v1))  # 5.0
#     print(bool(v1), bool(Vector2D()))  # True False
#
#     print(v1[0], v1[1])  # 3.0 4.0
#     print(len(v1))  # 2
#
#     print(sorted([v2, v1, Vector2D(0, 0)]))  # сортування за довжиною
#
#     # як ключ у словнику
#     points = {v1: "точка A", v2: "точка B"}
#     print(points[v1])  # точка A
#
#     # контекст-менеджер (наприклад, для логування чи тимчасового стану)
#     with v1:
#         print("робимо щось з вектором")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# + - * []
#
# g = Group("P45")
# g.add_student(s)
#
# print(g[0])
#
# p45 = p45 + p42

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Student:
#
#   def __init__(self, *grades):
#     self.grades = list(grades)
#
#   def __getitem__(self, index):
#     return self.grades[index]
#
# if __name__ == "__main__":
#   s = Student(2, 2, 2, 2, 2, 5, 5, 4, 3, 2, 12, 2, 2, 2)
#   print(s[0])
#   print(s[5])

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# def __del__(self):
#     """ some free memory operations """

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# типи зв'язків між класами:
# асоціація (будь яка згадка іншого типу в нашому класі)
# агрегування (Людина та Айфон)
# композиція (життєві цикли співпадають, Людина та Мозок)
# залежність (будь яка зміна в іншому класі призводить до змін в нашому класі)
# спадкування (в пайтоні є МНОЖИННЕ!!)
# реалізація (інтерфейсів нема в пайтоні, ABC, Protocol, динамічний поліморфізм в основному робиться завдяки duck typing)
# дружба (залишається тільки в С++)
# вкладеність (тіло одного класу повністю описане в тілі другого класу)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# dependency / association relationship example python

# class Person:
#     def __init__(self, name, surname=""):
#         self.name = name
#         self.surname = surname
#
#
# class Cat:
#     def __init__(self, nick, suit=""):
#         self.nick = nick
#         self.suit = suit # порода
#
#     def play_with(self, person: Person): # асоціація: кіт знає про людину (тимчасово)
#         print(f"Кіт {self.nick} грається з {person.name}")
#
#
# if __name__ == "__main__":
#     # об'єкти створюються незалежно один від одного
#     person = Person("Олександр")
#     cat = Cat("Локі", "сірий таббі")
#
#     # передаємо посилання на людину в метод кота
#     cat.play_with(person)
#
#     # обидва об'єкти можуть існувати окремо
#     del person # людина "зникла"
#     print(f"Кіт {cat.nick} все ще існує") # кіт живий

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# # aggregation example python
#
# class Hat:
#     def __init__(self, color="чорний", model="класичний", price=99.99):
#         self.color = color
#         self.model = model
#         self.price = price
#
#     def __str__(self):
#         return f"капелюх {self.model} кольору {self.color} за {self.price} грн"
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.hat: Hat = None # !!! агрегування !!! спочатку без капелюха
#
#     def take_hat(self, hat: Hat):
#         self.hat = hat
#         print(f"{self.name} надів {hat}")
#
#     def go_walk(self):
#         print(f"{self.name} пішов гуляти...")
#         if self.hat:
#             print("Раптово подув вітер... і капелюх полетів!")
#             self.hat = None # втрачаємо капелюх (але він не знищується)
#         else:
#             print("А капелюха й не було...")
#
#     def where_is_your_hat(self):
#         if self.hat:
#             print(f"Ось він! {self.hat}")
#         else:
#             print("Капелюха немає :(")
#
#
# if __name__ == "__main__":
#     nice_hat = Hat(color="сірий", model="фетровий", price=1799.0)
#     alex = Person("Олександр")
#
#     alex.take_hat(nice_hat)
#     alex.where_is_your_hat()
#
#     alex.go_walk()
#     alex.where_is_your_hat()
#
#     print(f"Але сам капелюх все ще існує: {nice_hat}")
#     print("Він може полетіти до когось іншого :)")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# composition example python

# class PegLeg:  # дерев'яна нога
#     def __init__(self):
#         self.color = "коричнева"
#         self.dirty = False
#         self.length = 14.5  # в дюймах
#         self.usability = 85  # 0–100
#         print(f"{self.__class__.__name__} створено")
#
#     def __del__(self):  # деструктор для демонстрації знищення об'єкта (частини)
#         print(f"{self.__class__.__name__} (дерев'яна нога) знищена")
#
#
# class HandHook:  # рука-гачок
#     def __init__(self):
#         self.material = "металева"
#         self.usability = 90
#         self.dirty = False
#         self.can_make_selfie = False
#         print(f"{self.__class__.__name__} створено")
#
#     def __del__(self):
#         print(f"{self.__class__.__name__} (гачок) знищено")
#
#
# class BlackEyePatch:  # наглазник
#     def __init__(self):
#         self.color = "чорний"
#         self.size = "XXL"
#         self.elastic = True
#         self.leather = True
#         print(f"{self.__class__.__name__} створено")
#
#     def __del__(self):
#         print(f"{self.__class__.__name__} (наглазник) знищено")
#
#
# class Pirate:
#     def __init__(self, name):
#         self.name = name
#
#         # композиція: частини створюються всередині класу Pirate
#         # і належать тільки цьому об'єкту
#         self.leg = PegLeg()
#         self.hand = HandHook()
#         self.patch = BlackEyePatch()
#
#         print(f"Пірат {self.name} створений\n")
#
#     def capture_ship(self):
#         print(f"{self.name}: Беремо на абордаж!!!")
#
#     def sing_song(self):
#         print(f"{self.name}: ...Йо-хо-хо, та пляшка рому!")
#
#     def __del__(self):  # деструктор для демонстрації знищення об'єкта (цілого)
#         print(f"Пірат {self.name} йде на дно...")
#
#         # при деструкції пірата знищуються і всі його частини (композиція)
#         # деструктори частин викличуться автоматично, бо посилання на них зникають
#
#
# if __name__ == "__main__":
#     p = Pirate("Капітан Джек Горобець")
#
#     p.capture_ship()
#     p.sing_song()
#
#     # явне видалення об'єкта для демонстрації деструктора
#     del p

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from dataclasses import dataclass
#
#
# @dataclass
# class Person:
#     name: str
#     age: int
#
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# @dataclass
# class Student(Person):
#     zalikova_book: dict | None
#
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# p = Person("Alex", 19)
# p.info()
#
# s = Student("Bob", 23, None)
# s.info()
# print(s.zalikova_book)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from dataclasses import dataclass
#
#
# class Person:
#     name: str
#     age: int
#
#     def __init__(self, name: str, age: int):
#         self.name = name
#         self.age = age
#         print("Person created")
#
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# @dataclass
# class Student(Person):
#     zalikova_book: dict | None
#
#     def __init__(self, name: str, age: int, zalikova_book: dict):
#         super().__init__(name, age)
#         self.zalikova_book = zalikova_book
#
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# p = Person("Alex", 19)
# p.info()
#
# s = Student("Bob", 23, None)
# s.info()
# print(s.zalikova_book)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# # An example of multiple inheritance in Python
#
# class JsonSerializable:
#     def to_json(self):
#         import json
#         return json.dumps(self.__dict__, ensure_ascii=False, indent=2)
#
#
# class Loggable:
#     def log(self, message):
#         print(f"[LOG {self.__class__.__name__}] {message}")
#
#
# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#
# class AdminUser(User, JsonSerializable, Loggable):
#     def __init__(self, name, email, permissions):
#         super().__init__(name, email)
#         self.permissions = permissions
#
#     def delete_user(self, user_id):
#         self.log(f"Адмін видалив користувача #{user_id}")
#
#
# admin = AdminUser("Олег", "oleg@admin.ua", ["full", "delete", "ban"])
# print(admin.to_json())
# admin.log("Система запущена")
# admin.delete_user(42)

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# MRO

# class A:
#     def say_hello(self):
#         print("Привіт з класу A")
#
#
# class B(A):
#     def say_hello(self):
#         print("Привіт з класу B")
#
#
# class C(A):
#     def say_hello(self):
#         print("Привіт з класу C")
#
#
# class D(B, C): # тут ромб
#     pass
#
#
# d = D()
# d.say_hello()  # виведеться Привіт з класу B
# print(D.mro()) # порядок пошуку методів
#
# # Python використовує MRO — Method Resolution Order (лінійний порядок розв’язання методів),
# # і за замовчуванням застосовує алгоритм C3 linearization https://www.geeksforgeeks.org/python/c3-linearization-algorithm-in-python/
# # шикарна стаття: https://habr.com/ru/articles/62203/
# # правила коротко:
# # 1) локальний порядок батьків у дужках зберігається: якщо class D(B, C), то B стоїть перед C у MRO
# # 2) монотонність: якщо в одній ієрархії A перед B, то ніде в похідних класах B не може опинитися перед A
# # 3) загальні предки йдуть після всіх своїх нащадків
# # тому порядок для D буде:
# # D > B > C > A > object

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# .__mro__       можно так подивитись точну послідовність

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class Clock:
#     def pikati(self):
#         print("бип-бип-бип! час вставати")
#
#
# class Cat:
#     def meow(self):
#         print("мяяяу!!")
#
#
# class CatAlarm(Clock, Cat):
#     def pikati(self):
#         print("будильник аларм мовчить котику немає до цього діла")
#
#     def meow(self):
#         print("Мяяяу давай їсти о 4 ранку кожаний")
#
#
# if __name__ == "__main__":
#     cat_alarm = CatAlarm()
#
#     cat_alarm.pikati()
#     cat_alarm.meow()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# sealed / final class

# # кастомний метаклас, який успадковується від вбудованого метакласу type
# # метаклас у Python — це клас, який створює (визначає поведінку створення) інші класи.
# # звичайний клас створює об'єкти (екземпляри), метаклас створює класи.
# class FinalMeta(type):
#     # перевизначаємо метод __new__ метакласу
#     # цей метод викликається, коли створюється новий клас
#     # cls   > це сам метаклас (тут FinalMeta)
#     # name  > ім'я класу, який зараз створюється (рядок)
#     # bases > кортеж базових класів (від кого успадковується)
#     # dct   > словник атрибутів та методів нового класу (namespace)
#     def __new__(cls, name, bases, dct):
#         # проходимо по всіх базових класах, від яких намагаються успадкувати
#         for base in bases:
#             # перевіряємо, чи є хоча б один базовий клас екземпляром нашого метакласу FinalMeta
#             # тобто чи намагаються успадкувати від класу, який сам створений через FinalMeta
#             if isinstance(base, FinalMeta):
#                 # якщо так — забороняємо створення такого класу
#                 # викидаємо помилку з поясненням, від якого саме класу не можна успадковувати
#                 raise TypeError(f"Не можна успадкуватися від фінального класу {base.__name__}")
#
#         # якщо жоден базовий клас не є "final" — дозволяємо створення класу
#         # викликаємо оригінальний __new__ від type, передаючи всі параметри
#         return super().__new__(cls, name, bases, dct)
#
#
# # приклад використання: створюємо "фінальний" клас
# # вказуємо, що цей клас має створюватися нашим метакласом FinalMeta
# class Terminal(metaclass=FinalMeta):
#     pass
#
#
# # спроба успадкування викличе помилку:
# class SubTerminal(Terminal):  # TypeError: Не можна успадкуватися від фінального класу Terminal

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# class FinalMeta(type):
#     def __new__(cls, name, bases, dct):
#         for base in bases:
#             if isinstance(base, FinalMeta):
#                 raise TypeError(f"даний тип є абстрактним")
#
#         return super().__new__(cls, name, bases, dct)
#
#
# class Terminal(metaclass=FinalMeta):
#     pass
#
#
# class SubTerminal(Terminal):
#     pass
#
# f = SubTerminal()

#////////////////////////////////////////////////////////////////////////////////////////////////////////

# An example of polymorphism in Python

# from random import Random
#
#
# # інтерфейсна роль виконується наявністю методів (duck typing)
# class Drivable:
#     def drive(self):
#         pass
#
#     def get_description(self):
#         pass
#
#
# # базовий клас (аналог abstract class)
# class Transport(Drivable):
#     def __init__(self, speed: float):
#         self.speed = speed
#
#     def get_speed(self) -> float:
#         return self.speed
#
#     def set_speed(self, speed: float):
#         self.speed = speed
#
#     # "абстрактний" метод (очікується, що дочірні класи його перевизначать)
#     def get_type(self) -> str:
#         raise NotImplementedError("Потрібно реалізувати в дочірньому класі")
#
#
# class Car(Transport):
#     def drive(self):
#         print(f"автомобіль їде зі швидкістю {self.speed:.1f} км/год")
#
#     def get_description(self) -> str:
#         return f"автомобіль зі швидкістю {self.speed:.1f} км/год"
#
#     def get_type(self) -> str:
#         return "автомобіль"
#
#
# class Bike(Transport):
#     def drive(self):
#         print(f"велосипед їде зі швидкістю {self.speed:.1f} км/год")
#
#     def get_description(self) -> str:
#         return f"велосипед зі швидкістю {self.speed:.1f} км/год"
#
#     def get_type(self) -> str:
#         return "велосипед"
#
#
# # поліморфна функція
# def drive_all(vehicles: list[Drivable]):
#     print("\nполіморфний виклик для всіх транспортних засобів:")
#     for vehicle in vehicles:
#         vehicle.drive()
#         print("опис:", vehicle.get_description())
#
#
# def main():
#     rnd = Random()
#
#     print("звичайний виклик:")
#     car = Car(120.0)
#     car.drive()
#     print("опис:", car.get_description())
#
#     # "апкастинг" (в python це просто використання базового типу)
#     print("\nприсвоєння об'єкта похідного класу змінній базового типу:")
#     bike: Transport = Bike(25.0)
#     bike.drive()
#     print("опис:", bike.get_description())
#
#     # поліморфний масив
#     print("\nполіморфний виклик через список:")
#     vehicles: list[Drivable] = []
#
#     for _ in range(5):
#         type_idx = rnd.randint(0, 1)
#         if type_idx == 0:
#             speed = 100.0 + rnd.random() * 50  # 100–150
#             vehicles.append(Car(speed))
#         elif type_idx == 1:
#             speed = 20.0 + rnd.random() * 10  # 20–30
#             vehicles.append(Bike(speed))
#
#     drive_all(vehicles)
#
#     print("\nвиведення типів транспорту:")
#     for v in vehicles:
#         print("тип:", v.get_type())
#
#
# if __name__ == "__main__":
#     main()

#/////////////////////////////////////////////////////////////////////////////////////////////////////////

# from dataclasses import dataclass
# from pathlib import Path
# import json
#
#
# @dataclass
# class User:
#     name: str
#     age: int
#
#     def to_json(self) -> str:
#         return json.dumps({"name": self.name, "age": self.age}, ensure_ascii=False)
#
#
# @dataclass
# class Product:
#     title: str
#     price: float
#
#     def to_json(self) -> str:
#         return json.dumps({"title": self.title, "price": self.price}, ensure_ascii=False)
#
#
# class ConfigFile:
#     def __init__(self, path: str | Path):
#         self.path = Path(path)
#
#     def to_json(self) -> str:
#         try:
#             return self.path.read_text(encoding="utf-8")
#         except FileNotFoundError:
#             return json.dumps({"error": f"Файл {self.path} не знайдено"}, ensure_ascii=False)
#
#
# # навіть рядок може "прикинутися" серіалізованим об'єктом
# class JsonString:
#     def __init__(self, raw: str):
#         self.raw = raw
#
#     def to_json(self) -> str:
#         return self.raw
#
#
# # функція, яка працює з будь-чим, що має .to_json()
# def save_to_api(obj) -> None:
#     try:
#         json_data = obj.to_json()
#         preview = json_data[:60].replace("\n", " ").strip()
#         print(f"Відправляємо на API: {preview}...")
#     except AttributeError:
#         print(f"Об'єкт {type(obj).__name__} не вміє .to_json() - пропускаємо")
#
# ###################################################################################
#
# objects = [
#     User("Олег", 29),
#     Product("Механічна клавіатура", 1899.90),
#     ConfigFile("settings.json"),          # якщо файлу немає, повернеться помилка в json
#     {"role": "admin", "active": True},    # dict — не має методу
#     Path("log.txt"),                      # Path — не має методу
#     JsonString('{"message": "Привіт!"}'), # рядок, що прикидається json
#     "звичайний текст",                    # str — теж не має .to_json()
# ]
#
# for item in objects:
#     save_to_api(item)

#////////////////////////////////////////////////////////////////////////////////////////////////////////

# # ABC example
#
# from abc import ABC, abstractmethod
# from dataclasses import dataclass
# from typing import final
#
#
# @dataclass
# class Notification:
#     title: str
#     message: str
#     recipient: str
#
#
# class NotificationSender(ABC):
#     """Базовий контракт для всіх способів відправки сповіщень"""
#
#     @abstractmethod
#     def send(self, notification: Notification) -> bool:
#         """Повертає True, якщо відправка успішна"""
#         pass
#
#     @abstractmethod
#     def get_channel_name(self) -> str:  # спробуйте прибрати метод :)
#         """Повертає назву каналу сповіщення"""
#         pass
#
#
# @final
# class TelegramSender(NotificationSender):
#     def send(self, notification: Notification) -> bool:
#         print(f"Telegram: {notification.recipient} | {notification.title}")
#         print(f"   {notification.message}")
#         return True
#
#     def get_channel_name(self) -> str:
#         return "Telegram"
#
#
# @final
# class EmailSender(NotificationSender):
#     def send(self, notification: Notification) -> bool:
#         print(f"Email: {notification.recipient} | {notification.title}")
#         print(f"   {notification.message[:60]}{'...' if len(notification.message) > 60 else ''}")
#         return True
#
#     def get_channel_name(self) -> str:
#         return "Email"
#
#
# ##########################################################################################################
#
# def notify_all(user_id: str, title: str, text: str, senders: list[NotificationSender]) -> None:
#     notification = Notification(title, text, user_id)
#
#     print(f"Надсилаємо сповіщення '{title}' користувачу {user_id}")
#     for sender in senders:
#         success = sender.send(notification)
#         print(f"Успішно через {sender.get_channel_name()}" if success
#               else f"Помилка в {sender.get_channel_name()}")
#
#
# senders = [TelegramSender(), EmailSender()]
# notify_all("@sunmeat", "Нова відповідь", "Твій коментар отримав 5 лайків!", senders)

#////////////////////////////////////////////////////////////////////////////////////////////////////////

# protocols in Python

# from typing import Protocol, runtime_checkable
# from dataclasses import dataclass
# from typing import final
#
#
# @dataclass
# class ServiceRequest:
#     service_type: str  # "доставка піци", "сантехнік", "електрик" тощо
#     address: str
#     details: str
#     customer_phone: str
#
#
# # декоратор із модуля typing, дозволяє використовувати протокол
# # у runtime-перевірках типу isinstance(obj, RequestNotifier).
# # без нього isinstance працюватиме тільки з ABC, а не з Protocol
# @runtime_checkable  # тут пайтон додає метод __instancecheck__ до метакласу протоколу
# # клас, який є протоколом (структурним типом).
# # успадкування від Protocol говорить: "це не звичайний клас,
# # а опис структури, яку будуть мати об'єкти"
# class RequestNotifier(Protocol):  # протокол - це опис структури, а не ієрархія успадкування
#     """Структурний контракт для каналів сповіщення клієнта про статус заявки"""
#
#     def send(self,
#              request: ServiceRequest) -> bool: ...  # оголошення методу send без реалізації ( ... — це вбудована константа типу Ellipsis) https://habr.com/ru/companies/otus/articles/716174/
#
#     # pass — "тут свідомо порожньо, і так має бути"
#     # ... - "тут щось має бути, але я ще не написав, повернуся потім колись"
#     def get_channel_name(self) -> str: ...
#
#
# @final
# class TelegramNotifier:
#     def send(self, request: ServiceRequest) -> bool:
#         print(f"Telegram: {request.customer_phone}")
#         print(f"Заявка: {request.service_type} | Адреса: {request.address}")
#         print(f"Деталі: {request.details}")
#         return True
#
#     def get_channel_name(self) -> str:
#         return "Telegram"
#
#
# @final
# class SmsNotifier:
#     def send(self, request: ServiceRequest) -> bool:
#         msg = f"Ваша заявка на {request.service_type} прийнята. Адреса: {request.address}. Деталі: {request.details[:60]}{'...' if len(request.details) > 60 else ''}"
#         print(f"SMS: {request.customer_phone} | {msg}")
#         return True
#
#     def get_channel_name(self) -> str:
#         return "SMS"
#
#
# ############################################################################################################################
#
# def notify_customer(phone: str, service: str, addr: str, details: str,
#
#                     # !!! список об’єктів, які відповідають протоколу RequestNotifier
#                     notifiers: list[RequestNotifier]) -> None:
#     request = ServiceRequest(service, addr, details, phone)
#
#     print(f"Повідомляємо клієнта {phone} про прийняття заявки на '{service}'")
#     for notifier in notifiers:
#         success = notifier.send(request)
#         print(f"Успішно через {notifier.get_channel_name()}" if success
#               else f"Помилка в {notifier.get_channel_name()}")
#
#
# # !!! список об’єктів, які відповідають протоколу RequestNotifier
# notifiers = [TelegramNotifier(), SmsNotifier()]
#
# notify_customer(
#     "+380630300035",
#     "доставка піци",
#     "вул. Дерибасівська, 12, кв. 45",
#     "Маргарита велика, без цибулі, додати подвійний сир",
#     notifiers
# )
#
# notify_customer(
#     "+380501234567",
#     "сантехнік",
#     "вул. Канатна, 8",
#     "Тече кран на кухні",
#     notifiers
# )
#
# # перевірка сумісності на етапі виконання
# print(isinstance(TelegramNotifier(), RequestNotifier))  # True
# print(isinstance(object(), RequestNotifier))  # False

#////////////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////////////////////////////////////////////////



#////////////////////////////////////////////////////////////////////////////////////////////////////////