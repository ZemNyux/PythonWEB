# lambda x,
#        y: x + y  # з точки зору пайтон, це просто звичайний вираз, як 1 + 2 або "hello", який НЕ вимагає обов’язкового «прив’язування» до імені чи контексту, як у більшості C-подібних мов
# print((lambda x: x ** 2)(5))  # 25 (викликається одразу після визначення)

###############################################################

# numbers = [1, 2, 3, 4, 5, 6]
# squared = list(map(lambda x: x ** 2, numbers))  # квадрати всіх чисел у списку
# evens = list(filter(lambda x: x % 2 == 0, numbers))  # лише парні числа зі списку
# print(squared)  # [1, 4, 9, 16, 25, 36]
# print(evens)  # [2, 4, 6]

###############################################################

# students = [
#     {'name': 'Анна', 'age': 25, 'grade': 11},
#     {'name': 'Владислав', 'age': 20, 'grade': 12},
#     {'name': 'Олександр', 'age': 20, 'grade': 10},
# ]
#
# # сортування спочатку за віком, потім за оцінкою (спадання)
# sorted_students = sorted(
#     students,
#     key=lambda s: (s['age'], -s['grade'])
# )
#
# for student in sorted_students:
#     print(student)

###############################################################

# chess_players = [
#     {'name': 'Свен Магнус Еєн Карлсен', 'country': 'NOR', 'elo': 2840,
#      'note': '5-разовий чемпіон світу, №1 світу багато років'},
#     {'name': 'Хікару Накамура', 'country': 'USA', 'elo': 2810, 'note': 'Топ-стрімер, блискавичний геній'},
#     {'name': 'Фабіано Каруана', 'country': 'USA', 'elo': 2795, 'note': 'Фіналіст ЧС 2018, стабільний топ-3'},
#     {'name': 'Вінсент Кеймер', 'country': 'GER', 'elo': 2776, 'note': 'Молодий німецький вундеркінд'},
#     {'name': 'Арджун Ерігайсі', 'country': 'IND', 'elo': 2775, 'note': 'Один з лідерів нової індійської хвилі'},
# ]
#
#
# # приклад функції вищого порядку: приймає список і функцію-порівняння (стратегію)
# def find_extreme(players, compare_func):
#     """
#     повертає 'найкращий' елемент за заданою функцією порівняння.
#     compare_func(a, b) буде True, якщо a 'кращий' за b.
#     """
#     if not players:
#         return None
#
#     best = players[0]
#     for player in players[1:]:
#         if compare_func(player, best):
#             best = player
#     return best
#
#
# # хто має найвищий Elo
# best_by_elo = find_extreme(
#     chess_players,
#     lambda a, b: a['elo'] > b['elo']
# )
#
# print("\n\nНайсильніший за Elo:")
# print(f"{best_by_elo['name']} ({best_by_elo['country']}) — {best_by_elo['elo']} Elo")
# print(f"Примітка: {best_by_elo['note']}\n")
#
# # хто має найдовше ім'я (інша стратегія через лямбду)
# longest_name = find_extreme(
#     chess_players,
#     lambda a, b: len(a['name']) > len(b['name'])
# )
#
# print("Гравець з найдовшим ім'ям:")
# print(f"{longest_name['name']} — {len(longest_name['name'])} символів")
#
# # вивід усього списку по одному гравцю на рядок
# print("\nПовний список (відсортований за Elo спаданням):")
# sorted_players = sorted(chess_players, key=lambda p: p['elo'], reverse=True)
#
# for p in sorted_players:
#     print(f"{p['name']:<23} | {p['country']} | Elo: {p['elo']} | {p['note']}")