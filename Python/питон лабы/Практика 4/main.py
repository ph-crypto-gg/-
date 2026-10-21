from models import Course
from services import CourseService
from exceptions import CourseError
from storage import load, save


def main():
    try:
        service = CourseService(load())
    except (OSError, ValueError, TypeError, CourseError) as error:
        print("Не удалось загрузить данные:", error)
        return

    while True:
        print("\n1 Создать курс; 2 Добавить студента; 3 Удалить студента")
        print("4 Найти курс; 5 Средняя загрузка; 6 Все курсы; 7 Сохранить; 0 Выход")
        choice = input("Действие: ")
        try:
            if choice == "1":
                course = Course(input("Название: "), input("Преподаватель: "),
                                int(input("Часы: ")), float(input("Стоимость: ")))
                service.create(course)
            elif choice == "2":
                service.add_student(input("Курс: "), input("Студент: "))
            elif choice == "3":
                service.remove_student(input("Курс: "), input("Студент: "))
            elif choice == "4":
                print(service.find(input("Курс: ")))
            elif choice == "5":
                print("Среднее количество студентов на курс:", service.average_load())
            elif choice == "6":
                for course in service.courses:
                    print(course)
            elif choice == "7":
                save(service.courses)
                print("Сохранено")
            elif choice == "0":
                save(service.courses)
                break
            else:
                print("Неизвестное действие")
        except (CourseError, ValueError, OSError) as error:
            print("Ошибка:", error)


if __name__ == "__main__":
    main()
