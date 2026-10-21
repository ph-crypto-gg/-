def show(dishes):
    """Вывод списка блюд."""
    if not dishes:
        print("Список пуст.")
        return
    for d in dishes:
        print(f"{d['name']:<15} | {d['category']:<10} | "
              f"{d['price']:>8.2f} руб. | {d['calories']:>5} ккал")


def add(dishes):
    """Добавление блюда."""
    name = input("Название: ").strip()
    category = input("Категория: ").strip()
    try:
        price = float(input("Цена: "))
        cal = int(input("Калорийность: "))
    except ValueError:
        print("Ошибка ввода.")
        return
    dishes.append({"name": name, "category": category,
                   "price": price, "calories": cal})
    print("Добавлено.")


def find(dishes, category):
    """Поиск по категории (list comprehension)."""
    return [d for d in dishes if d["category"].lower() == category.lower()]


def filtr(dishes, max_cal):
    """Фильтр по калорийности (list comprehension)."""
    return [d for d in dishes if d["calories"] <= max_cal]


def stats(dishes):
    """Статистика."""
    if not dishes:
        print("Нет данных.")
        return
    g = sum(d["price"] for d in dishes) / len(dishes)
    top = max(dishes, key=lambda d: d["price"])
    print(f"Всего: {len(dishes)}")
    print(f"Средняя цена: {avg:.2f} руб.")
    print(f"Самое дорогое: {top['name']} ({top['price']:.2f} руб.)")
    print(f"Мин. калорийность: {min(d['calories'] for d in dishes)}")
    print(f"Макс. калорийность: {max(d['calories'] for d in dishes)}")


def main():
    dishes = [
        {"name": "Борщ",     "category": "суп",     "price": 250.0, "calories": 180},
        {"name": "Цезарь",   "category": "салат",   "price": 320.0, "calories": 250},
        {"name": "Стейк",    "category": "горячее", "price": 890.0, "calories": 620},
        {"name": "Тирамису", "category": "десерт",  "price": 280.0, "calories": 340},
        {"name": "Окрошка",  "category": "суп",     "price": 220.0, "calories": 140},
    ]

    menu = {
        "1": ("Добавить",        lambda: add(dishes)),
        "2": ("Показать все",    lambda: show(dishes)),
        "3": ("Поиск по кат.",   lambda: show(find(dishes, input("Категория: ")))),
        "4": ("Фильтр по кал.",  lambda: show(filtr(dishes, int(input("Макс. ккал: "))))),
        "5": ("Сортировка",      lambda: show(sorted(dishes, key=lambda d: d["price"]))),
        "6": ("Статистика",      lambda: stats(dishes)),
        "7": ("Уникальные кат.", lambda: print(*sorted({d["category"] for d in dishes}), sep="\n")),
    }

    while True:
        print("\n=== МЕНЮ ===")
        for k, (name, _) in menu.items():
            print(f"{k}. {name}")
        print("0. Выход")

        choice = input("Выбор: ").strip()
        if choice == "0":
            break
        elif choice in menu:
            menu[choice][1]()
        else:
            print("Неверный пункт.")


if __name__ == "__main__":
    main()