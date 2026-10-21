from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    CREATED = "создана"
    ACCEPTED = "принята"
    MOVING = "в пути"
    DELIVERED = "доставлена"
    CANCELLED = "отменена"


@dataclass
class Entity:
    id: int
    name: str

    def report(self) -> str:
        return f"{self.id}: {self.name}"


@dataclass
class Courier(Entity):
    phone: str

    def report(self) -> str:
        return f"Курьер {self.name}, телефон {self.phone}"


@dataclass
class Parcel(Entity):
    weight: float

    def report(self) -> str:
        return f"Посылка {self.name}, {self.weight} кг"


@dataclass
class Delivery:
    id: int
    courier: Courier
    parcel: Parcel
    distance: float
    duration: float = 0
    status: Status = Status.CREATED
