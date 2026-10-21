import pytest
from repository import MemoryRepository
from services import DeliveryService
from patterns import DeliveryFactory, Documents, StandardPricing, UrgentPricing, EconomyPricing


def make_delivery():
    return DeliveryFactory.create("документы", 1, "Дом", 2, 5)


def test_factory():
    assert isinstance(make_delivery(), Documents)


def test_invalid_factory():
    with pytest.raises(ValueError):
        DeliveryFactory.create("неизвестный", 1, "Дом", 2, 5)


@pytest.mark.parametrize("pricing, cost", [(StandardPricing(), 220),
                                         (UrgentPricing(), 330), (EconomyPricing(), 176)])
def test_strategy(pricing, cost):
    service = DeliveryService(MemoryRepository(), pricing)
    service.create(make_delivery())
    assert service.cost(1) == cost


def test_repository():
    repository = MemoryRepository()
    repository.add(make_delivery())
    repository.delete(1)
    assert repository.get_all() == []


def test_observer():
    messages = []
    class Recorder:
        def update(self, delivery):
            messages.append(delivery.status)
    service = DeliveryService(MemoryRepository(), StandardPricing())
    service.create(make_delivery())
    service.subscribe(Recorder())
    service.change_status(1, "принята")
    assert messages == ["принята"]
