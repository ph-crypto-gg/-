from dataclasses import dataclass
from typing import Protocol
from models import Delivery


@dataclass
class Documents(Delivery):
    kind: str = "документы"


@dataclass
class Parcel(Delivery):
    kind: str = "посылка"


@dataclass
class LargeCargo(Delivery):
    kind: str = "крупный груз"


class DeliveryFactory:
    types = {"документы": Documents, "посылка": Parcel, "крупный груз": LargeCargo}

    @staticmethod
    def create(kind: str, id: int, address: str, weight: float, distance: float) -> Delivery:
        if kind not in DeliveryFactory.types:
            raise ValueError("Неизвестный вид груза")
        return DeliveryFactory.types[kind](id, address, weight, distance)


class Pricing(Protocol):
    def calculate(self, delivery: Delivery) -> float: ...


class StandardPricing:
    def calculate(self, delivery: Delivery) -> float:
        return 100 + delivery.distance * 20 + delivery.weight * 10


class UrgentPricing:
    def calculate(self, delivery: Delivery) -> float:
        return StandardPricing().calculate(delivery) * 1.5


class EconomyPricing:
    def calculate(self, delivery: Delivery) -> float:
        return StandardPricing().calculate(delivery) * 0.8


class Observer(Protocol):
    def update(self, delivery: Delivery) -> None: ...


class ClientObserver:
    def update(self, delivery: Delivery) -> None:
        print(f"Клиент: доставка {delivery.id} — {delivery.status.value}")


class CourierObserver:
    def update(self, delivery: Delivery) -> None:
        print(f"Курьер {delivery.courier}: доставка {delivery.id} — {delivery.status.value}")
