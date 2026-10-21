# До паттернов: выбор груза, тарифа и уведомлений смешан в одной функции.
def delivery_cost(kind, tariff, distance, weight, status):
    if kind == "документы":
        item = {"kind": "документы", "weight": weight}
    elif kind == "посылка":
        item = {"kind": "посылка", "weight": weight}
    elif kind == "крупный груз":
        item = {"kind": "крупный груз", "weight": weight}
    else:
        raise ValueError("Неизвестный груз")
    cost = 100 + distance * 20 + item["weight"] * 10
    if tariff == "срочная":
        cost *= 1.5
    elif tariff == "экономичная":
        cost *= 0.8
    elif tariff != "стандартная":
        raise ValueError("Неизвестный тариф")
    print("Клиент:", status)
    print("Курьер:", status)
    return cost
