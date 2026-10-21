months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн", 
          "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]

water = []
print("Введите расход воды (куб.м) по месяцам:")
for m in months:
    while True:
        try:
            val = float(input(f"{m}: "))
            if val >= 0:
                water.append(val)
                break
            print("Не может быть отрицательным!")
        except:
            print("Введите число!")

total = sum(water)

avg = total / 12

max_val = max(water)
max_month = months[water.index(max_val)]

norm = float(input("Введите норму расхода (куб.м): "))
above = sum(1 for w in water if w > norm)

tariff = float(input("Введите тариф (руб/куб.м): "))
cost = total * tariff
print()
print(f"Общий расход: {total:.2f} куб.м")
print(f"Средний расход: {avg:.2f} куб.м")
print(f"Максимум: {max_month} ({max_val:.2f} куб.м)")
print(f"Месяцев выше нормы ({norm}): {above}")
print(f"Стоимость воды: {cost:.2f} руб.")
