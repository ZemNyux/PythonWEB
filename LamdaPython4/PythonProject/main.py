import datetime

# список кортежів
STORES = [
    (45.351, 28.840, "Сільпо Ізмаїл, вул. Миколи Аркаса"),
    (46.482, 30.732, "Сільпо Одеса, Таїровське"),
    (50.450, 30.523, "Сільпо Київ, Поділ"),
]

PRODUCTS = [
    ("4601234000012", "Молоко 'Яготинське' 2.5%", 36.90, "Молочні продукти"),
    ("4820024940017", "Хліб 'Київхліб' нарізний", 24.50, "Хлібобулочні вироби"),
    ("5900334012345", "Печиво 'Світоч' Ювілейне", 42.99, "Солодощі"),
]

# кортежі в якості "енамів"
STATES = ("PENDING", "RUNNING", "SUCCESS", "FAILED")
ACTIONS = ((0, "create"), (1, "update"), (2, "delete"))


# пошук товару за штрихкодом
def find_product(barcode):
    for product in PRODUCTS:
        if product[0] == barcode:
            return product[1], product[2], product[3]  # повернення трьох значень
    return "Товар не знайдено", 0.0, "—"


def build_receipt(cart):
    receipt = []

    for barcode, quantity in cart:
        name, price, category = find_product(barcode)
        if price == 0:
            continue

        subtotal = round(price * quantity, 2)
        receipt.append((name, price, quantity, subtotal, category))

    return receipt


def print_receipt(receipt):
    if not receipt:
        print("Кошик порожній")
        return

    lat, lon, store_name = STORES[0]  # розпакування кортежу

    total = 0.0

    print("\n" + "═" * 70)
    print("Чек:")
    print(f"Магазин: {store_name}  ({lat:.3f}, {lon:.3f})")
    print(f"Дата: {datetime.date.today()}")
    print("─" * 70)
    print(f"{'Назва товару':<24} {'Ціна':>8} {'шт':>6} {'Сума':>9} {'Категорія':<15}")
    print("─" * 70)

    for name, price, qty, subtotal, category in receipt:
        print(f"{name:<24} {price:8.2f} {qty:6d} {subtotal:9.2f} {category:<15}")
        total += subtotal

    print("─" * 70)
    print(f"{'РАЗОМ':<55} {total:10.2f} грн")
    print("═" * 70)


if __name__ == "__main__":
    my_cart = [
        ("4601234000012", 2),  # 2 молока
        ("4820024940017", 1),  # 1 хліб
        ("5900334012345", 3),  # 3 пачки печива
    ]

    receipt = build_receipt(my_cart)

    print_receipt(receipt)

    print("\nПриклади кортежів як енамів:")
    print("Статуси:", STATES)
    print("Поточний статус:", STATES[2])  # SUCCESS
    print("Дії:", [action[1] for action in ACTIONS])
    print("Обрана дія:", ACTIONS[1][1])  # update