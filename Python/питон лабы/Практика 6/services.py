from models import Delivery, Status
from decorators import log, timed, require_status


class DeliveryNotFound(Exception):
    pass


class DeliveryService:
    def __init__(self) -> None:
        self.deliveries: list[Delivery] = []

    @log
    def add(self, delivery: Delivery) -> None:
        if delivery.id <= 0 or delivery.distance < 0 or delivery.parcel.weight <= 0:
            raise ValueError("Неверные параметры доставки")
        if any(d.id == delivery.id for d in self.deliveries):
            raise ValueError("Этот id уже существует")
        self.deliveries.append(delivery)

    def find(self, id: int) -> Delivery:
        for delivery in self.deliveries:
            if delivery.id == id:
                return delivery
        raise DeliveryNotFound("Доставка не найдена")

    def delete(self, id: int) -> None:
        self.deliveries.remove(self.find(id))

    def change_status(self, id: int, status: Status) -> None:
        delivery = self.find(id)
        allowed = {Status.CREATED: [Status.ACCEPTED, Status.CANCELLED],
                   Status.ACCEPTED: [Status.MOVING, Status.CANCELLED],
                   Status.MOVING: [Status.DELIVERED, Status.CANCELLED]}
        if status not in allowed.get(delivery.status, []):
            raise ValueError("Недопустимый переход статуса")
        if status == Status.DELIVERED:
            raise ValueError("Используйте пункт завершения доставки")
        delivery.status = status

    @require_status(Status.MOVING)
    def finish(self, delivery: Delivery, duration: float) -> None:
        if duration <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        delivery.duration = duration
        delivery.status = Status.DELIVERED

    def cost(self, delivery: Delivery) -> float:
        return 100 + delivery.distance * 20 + delivery.parcel.weight * 10

    @timed
    def statistics(self) -> dict:
        completed = [d for d in self.deliveries if d.status == Status.DELIVERED]
        average = sum(d.duration for d in completed) / len(completed) if completed else 0
        return {"всего": len(self.deliveries), "доставлено": len(completed),
                "средняя продолжительность, мин": average}
