class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum([sum(values) / len(values) for values in self.grades.values()]) / len(self.grades)}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return (sum([sum(values) / len(values) for values in self.grades.values()]) / len(self.grades)) < (
                    sum([sum(values) / len(values) for values in other.grades.values()]) / len(other.grades))


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum([sum(values) / len(values) for values in self.grades.values()]) / len(self.grades)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return (sum([sum(values) / len(values) for values in self.grades.values()]) / len(self.grades)) < (
                    sum([sum(values) / len(values) for values in other.grades.values()]) / len(other.grades))


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Создание экземпляров каждого класса
student1 = Student('Student', 'One', 'Male')
student2 = Student('Student', 'Two', 'Female')
lecturer1 = Lecturer('Lecturer', 'One')
lecturer2 = Lecturer('Lecturer', 'Two')
reviewer1 = Reviewer('Reviewer', 'One')
reviewer2 = Reviewer('Reviewer', 'Two')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

# Выставление оценок
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)


# Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def avg_grade_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count != 0 else 0


def avg_grade_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count != 0 else 0


print(avg_grade_students([student1, student2],
                         'Python'))  # Средняя оценка за домашние задания по всем студентам в рамках конкретного курса
print(avg_grade_lecturers([lecturer1, lecturer2], 'Python'))  # Средняя оценка за лекции всех лекторов в рамках курса
