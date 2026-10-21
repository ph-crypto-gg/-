from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    CREATED = "создана"
    ACCEPTED = "принята"
    MOVING = "в пути"
    DELIVERED = "доставлена"
    CANCELLED = "отменена"


@dataclass
class Delivery:
    id: int
    address: str
    weight: float
    distance: float
    courier: str = ""
    status: Status = Status.CREATED


@dataclass
class DocumentDelivery(Delivery):
    document_count: int = 1


@dataclass
class ParcelDelivery(Delivery):
    fragile: bool = False
