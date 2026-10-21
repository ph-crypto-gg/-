class Course:
    def __init__(self, name, teacher, hours, price, students):
        if hours <= 0 or price < 0 or students < 0:
            raise ValueError("Неверные данные курса")
        self.name = name
        self.teacher = teacher
        self.hours = hours
        self.price = price
        self.students = students

    def __repr__(self):
        return f"{self.name}: {self.price} руб., {self.students} студентов"


class OnlineCourse(Course):
    def format(self):
        return "Онлайн"


class ClassroomCourse(Course):
    def format(self):
        return "В аудитории"
