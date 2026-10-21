import pytest
from models import Delivery
from repository import MemoryRepository
from services import DeliveryService


class FakeNotifier:
    def __init__(self):
        self.messages = []

    def send(self, message):
        self.messages.append(message)


@pytest.fixture
def service():
    return DeliveryService(MemoryRepository(), FakeNotifier())


def test_create(service):
    service.create(Delivery(1, "Дом", 2, 5))
    assert service.repository.get(1).address == "Дом"


def test_invalid(service):
    with pytest.raises(ValueError):
        service.create(Delivery(1, "Дом", -2, 5))


def test_assign(service):
    service.create(Delivery(1, "Дом", 2, 5))
    service.assign(1, "Иван")
    assert service.repository.get(1).courier == "Иван"


def test_cost(service):
    service.create(Delivery(1, "Дом", 2, 5))
    assert service.cost(1) == 220


def test_notification(service):
    service.create(Delivery(1, "Дом", 2, 5))
    service.change_status(1, "принята")
    assert service.notifier.messages == ["Доставка 1: принята"]


def test_invalid_transition(service):
    service.create(Delivery(1, "Дом", 2, 5))
    with pytest.raises(ValueError):
        service.change_status(1, "доставлена")
