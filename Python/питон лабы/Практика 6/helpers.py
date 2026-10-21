from contextlib import contextmanager
from time import perf_counter
from typing import Protocol
from models import Entity


class Reportable(Protocol):
    def report(self) -> str: ...


def show_report(item: Reportable) -> None:
    print(item.report())


@contextmanager
def operation(name: str):
    start = perf_counter()
    print("Начало:", name)
    try:
        yield
    finally:
        print(f"Конец: {name}, {perf_counter() - start:.6f} с")


def inspect_object(item: object) -> None:
    print("Тип:", type(item).__name__)
    print("Это Entity:", isinstance(item, Entity))
    print("Есть id:", hasattr(item, "id"))
    print("Значение id:", getattr(item, "id", None))
    print("Публичные имена:", [name for name in dir(item) if not name.startswith("_")])
