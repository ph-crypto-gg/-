from models import Courier, Parcel, Delivery, Status
from services import DeliveryService, DeliveryNotFound
from helpers import operation, show_report, inspect_object


def main() -> None:
    service = DeliveryService()
    courier = Courier(1, "Максим", "9001234567")
    show_report(courier)
    while True:
        print("\n1 Добавить; 2 Удалить; 3 Найти; 4 Все; 5 Статус")
        print("6 Стоимость; 7 Завершить; 8 Статистика; 9 Интроспекция; 10 Демонстрация; 0 Выход")
        choice = input("Действие: ")
        try:
            if choice == "0":
                break
            if choice == "1":
                id = int(input("id: "))
                parcel = Parcel(id, input("Посылка: "), float(input("Вес, кг: ")))
                service.add(Delivery(id, courier, parcel, float(input("Расстояние, км: "))))
            elif choice == "4":
                for delivery in service.deliveries:
                    print(delivery)
            elif choice == "8":
                print(service.statistics())
            elif choice == "10":
                with operation("Демонстрация"):
                    parcel = Parcel(1, "Книга", 1)
                    show_report(parcel)
                    demo = DeliveryService()
                    delivery = Delivery(1, courier, parcel, 5)
                    demo.add(delivery)
                    demo.change_status(1, Status.ACCEPTED)
                    demo.change_status(1, Status.MOVING)
                    demo.finish(delivery, 30)
                    print(demo.statistics())
            elif choice in ("2", "3", "5", "6", "7", "9"):
                delivery = service.find(int(input("id: ")))
                if choice == "2":
                    service.delete(delivery.id)
                elif choice == "3":
                    print(delivery)
                elif choice == "5":
                    print([s.value for s in Status])
                    service.change_status(delivery.id, Status(input("Статус: ")))
                elif choice == "6":
                    print("Стоимость:", service.cost(delivery))
                elif choice == "7":
                    service.finish(delivery, float(input("Продолжительность, мин: ")))
                elif choice == "9":
                    inspect_object(delivery)
            else:
                print("Неизвестное действие")
        except (ValueError, DeliveryNotFound) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
