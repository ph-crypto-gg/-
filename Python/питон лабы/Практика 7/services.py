from typing import Protocol
from models import Delivery, Status
from repository import Repository


class Notifier(Protocol):
    def send(self, message: str) -> None: ...


class EmailNotifier:
    def send(self, message: str) -> None:
        print("Email (учебный вывод):", message)


class SmsNotifier:
    def send(self, message: str) -> None:
        print("SMS (учебный вывод):", message)


class DeliveryService:
    def __init__(self, repository: Repository, notifier: Notifier) -> None:
        self.repository = repository
        self.notifier = notifier

    def create(self, delivery: Delivery) -> None:
        if delivery.id <= 0 or not delivery.address or delivery.weight <= 0 or delivery.distance < 0:
            raise ValueError("Некорректная доставка")
        self.repository.add(delivery)

    def assign(self, id: int, courier: str) -> None:
        if not courier:
            raise ValueError("Укажите курьера")
        self.repository.get(id).courier = courier

    def change_status(self, id: int, status: str) -> None:
        delivery = self.repository.get(id)
        transitions = {"создана": ["принята", "отменена"],
                       "принята": ["в пути", "отменена"],
                       "в пути": ["доставлена", "отменена"]}
        if status not in transitions.get(delivery.status, []):
            raise ValueError("Недопустимый переход статуса")
        if status == "в пути" and not delivery.courier:
            raise ValueError("Сначала назначьте курьера")
        delivery.status = Status(status)
        self.notifier.send(f"Доставка {id}: {status}")

    def cost(self, id: int) -> float:
        delivery = self.repository.get(id)
        return 100 + delivery.distance * 20 + delivery.weight * 10
