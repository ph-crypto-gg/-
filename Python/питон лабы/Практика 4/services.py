from exceptions import CourseError


class CourseService:
    def __init__(self, courses):
        self.courses = courses

    def create(self, course):
        if any(c.name == course.name for c in self.courses):
            raise CourseError("Такой курс уже есть")
        self.courses.append(course)

    def find(self, name):
        for course in self.courses:
            if course.name == name:
                return course
        raise CourseError("Курс не найден")

    def add_student(self, name, student):
        course = self.find(name)
        if not student or student in course.students:
            raise CourseError("Пустое имя или студент уже записан")
        course.students.append(student)

    def remove_student(self, name, student):
        course = self.find(name)
        if student not in course.students:
            raise CourseError("Студент не найден")
        course.students.remove(student)

    def average_load(self):
        if not self.courses:
            return 0
        return sum(len(c.students) for c in self.courses) / len(self.courses)
