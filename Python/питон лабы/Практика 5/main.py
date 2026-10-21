from models import OnlineCourse, ClassroomCourse
from operations import filter_objects, transform_objects, sort_objects, average_price
from generators import teacher_courses


def main():
    courses = [OnlineCourse("Python", "Иванов", 40, 5000, 18),
               ClassroomCourse("Математика", "Петров", 60, 6000, 35),
               OnlineCourse("SQL", "Иванов", 30, 4000, 12)]
    try:
        price = float(input("Максимальная стоимость: "))
        capacity = int(input("Максимум студентов на курс: "))
        if price < 0 or capacity <= 0:
            raise ValueError("Стоимость неотрицательна, вместимость положительна")
        print("По стоимости:", filter_objects(courses, lambda c: c.price <= price))
        print("Названия:", transform_objects(courses, lambda c: c.name))
        print("По числу студентов:", sort_objects(courses, lambda c: c.students))
        print("Средняя стоимость:", average_price(courses))
        print("Есть переполненные:", any(c.students > capacity for c in courses))
        print("Форматы:", [c.format() for c in courses])
        teacher = input("Преподаватель: ")
        for course in teacher_courses(courses, teacher):
            print(course)
    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()
