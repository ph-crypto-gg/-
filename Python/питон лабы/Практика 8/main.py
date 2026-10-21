from repository import MemoryRepository
from services import DeliveryService
from patterns import (DeliveryFactory, StandardPricing, UrgentPricing, EconomyPricing,
                      ClientObserver, CourierObserver)


def main() -> None:
    repository = MemoryRepository()
    service = DeliveryService(repository, StandardPricing())
    service.subscribe(ClientObserver())
    service.subscribe(CourierObserver())
    for id, kind in enumerate(DeliveryFactory.types, 1):
        delivery = DeliveryFactory.create(kind, id, "ул. Пушкина, 10", id, 5)
        delivery.courier = "Максим"
        service.create(delivery)
        print(delivery)
    for pricing in (StandardPricing(), UrgentPricing(), EconomyPricing()):
        service.pricing = pricing
        print(type(pricing).__name__, service.cost(1))
    service.change_status(1, "принята")
    service.change_status(1, "в пути")


if __name__ == "__main__":
    main()
