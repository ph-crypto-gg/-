from models import Delivery, Status
from repository import Repository
from patterns import Pricing, Observer


class DeliveryService:
    def __init__(self, repository: Repository, pricing: Pricing) -> None:
        self.repository = repository
        self.pricing = pricing
        self.observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def create(self, delivery: Delivery) -> None:
        if delivery.id <= 0 or not delivery.address or delivery.weight <= 0 or delivery.distance < 0:
            raise ValueError("Некорректная доставка")
        self.repository.add(delivery)

    def cost(self, id: int) -> float:
        return self.pricing.calculate(self.repository.get(id))

    def change_status(self, id: int, status: str) -> None:
        delivery = self.repository.get(id)
        transitions = {"создана": ["принята", "отменена"],
                       "принята": ["в пути", "отменена"],
                       "в пути": ["доставлена", "отменена"]}
        if status not in transitions.get(delivery.status, []):
            raise ValueError("Недопустимый переход")
        delivery.status = Status(status)
        for observer in self.observers:
            observer.update(delivery)
