# До SOLID: хранение, расчёт и уведомление смешаны в одном классе.
class BigInterface:
    def save(self):
        raise NotImplementedError

    def send_sms(self):
        raise NotImplementedError

    def print_report(self):
        raise NotImplementedError


class ConsoleNotifier(BigInterface):
    def send_sms(self):
        print("SMS отправлено (учебный вывод)")
    # save и print_report этому уведомителю не нужны: нарушение ISP.


class BadCourier:
    def deliver(self):
        return "Доставка выполнена"


class OfficeWorker(BadCourier):
    def deliver(self):
        raise ValueError("Офисный сотрудник не доставляет посылки")
    # Подтип не заменяет курьера: нарушение LSP.


class BadDeliveryService:
    def __init__(self):
        self.items = {}
        self.notifier = ConsoleNotifier()  # Жёсткая зависимость: нарушение DIP.

    def create(self, id, address, weight, distance):
        self.items[id] = dict(address=address, weight=weight, distance=distance,
                              courier="", status="создана")

    def assign(self, id, courier):
        self.items[id]["courier"] = courier

    def change_status(self, id, status, notification):
        item = self.items[id]
        transitions = {"создана": ["принята", "отменена"],
                       "принята": ["в пути", "отменена"],
                       "в пути": ["доставлена", "отменена"]}
        if status not in transitions.get(item["status"], []):
            raise ValueError("Недопустимый переход")
        if status == "в пути" and not item["courier"]:
            raise ValueError("Нет курьера")
        item["status"] = status
        if notification == "email":
            print("Email:", status)
        elif notification == "sms":
            print("SMS:", status)

    def cost(self, id):
        item = self.items[id]
        return 100 + item["distance"] * 20 + item["weight"] * 10
