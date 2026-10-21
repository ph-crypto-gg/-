from models import DocumentDelivery, ParcelDelivery
from repository import MemoryRepository
from services import DeliveryService, EmailNotifier, SmsNotifier


def main() -> None:
    for notifier in (EmailNotifier(), SmsNotifier()):
        repository = MemoryRepository()
        service = DeliveryService(repository, notifier)
        service.create(DocumentDelivery(1, "ул. Пушкина, 10", 2, 5, document_count=3))
        service.create(ParcelDelivery(2, "ул. Ленина, 5", 4, 8, fragile=True))
        service.assign(1, "Максим")
        service.change_status(1, "принята")
        service.change_status(1, "в пути")
        print("Стоимость:", service.cost(1))
        print(repository.get_all())


if __name__ == "__main__":
    main()
