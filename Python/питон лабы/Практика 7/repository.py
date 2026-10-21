from typing import Protocol
from models import Delivery


class Reader(Protocol):
    def get(self, id: int) -> Delivery: ...
    def get_all(self) -> list[Delivery]: ...


class Writer(Protocol):
    def add(self, delivery: Delivery) -> None: ...
    def delete(self, id: int) -> None: ...


class Repository(Reader, Writer, Protocol):
    pass


class MemoryRepository:
    def __init__(self) -> None:
        self.items: dict[int, Delivery] = {}

    def add(self, delivery: Delivery) -> None:
        if delivery.id in self.items:
            raise ValueError("id уже существует")
        self.items[delivery.id] = delivery

    def get(self, id: int) -> Delivery:
        if id not in self.items:
            raise ValueError("Доставка не найдена")
        return self.items[id]

    def get_all(self) -> list[Delivery]:
        return list(self.items.values())

    def delete(self, id: int) -> None:
        self.get(id)
        del self.items[id]
