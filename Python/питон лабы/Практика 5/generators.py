def teacher_courses(courses, teacher):
    for course in courses:
        if course.teacher == teacher:
            yield course
