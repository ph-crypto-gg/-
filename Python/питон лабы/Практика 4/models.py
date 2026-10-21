from exceptions import CourseError


class Course:
    def __init__(self, name, teacher, hours, price, students=None):
        if not name or not teacher or hours <= 0 or price < 0:
            raise CourseError("Неверные данные курса")
        self.name = name
        self.teacher = teacher
        self.hours = hours
        self.price = price
        self.students = students if students is not None else []

    def __str__(self):
        return f"{self.name}: {self.teacher}, {self.hours} ч, {self.price} руб., {self.students}"
