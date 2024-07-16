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
        self.lecture_grades = {}

    def __str__(self):
        average_grade = sum(sum(grades) for grades in self.lecture_grades.values()) / len(self.lecture_grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def average_grade(self):
        if not self.lecture_grades:
            return 0
        else:
            total_sum = sum(sum(grades) for grades in self.lecture_grades.values())
            total_count = sum(len(grades) for grades in self.lecture_grades.values())
            return total_sum / total_count


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nУ проверяющих:'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if not self.grades:
            average_grade = 0
        else:
            total_sum = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            average_grade = total_sum / total_count

        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def average_grade(self):
        if not self.grades:
            return 0
        else:
            total_sum = sum(sum(grades) for grades in self.grades.values())
            total_count = sum(len(grades) for grades in self.grades.values())
            return total_sum / total_count


# Создаем экземпляры объектов
student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student1.grades = {'Python': [10, 8, 9], 'Git': [9, 7]}

student2 = Student('Alice', 'Wonderland', 'female')
student2.courses_in_progress = ['Python', 'C++']
student2.finished_courses = ['Алгоритмы и структуры данных']
student2.grades = {'Python': [8, 9, 7], 'C++': [10, 8]}

lecturer1 = Lecturer('John', 'Doe')
lecturer1.lecture_grades = {'Python': [10, 9, 9, 8]}
lecturer2 = Lecturer('Jane', 'Smith')
lecturer2.lecture_grades = {'Python': [9, 8, 9, 7]}

reviewer1 = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Another', 'Reviewer')

# Вывод информации
print("Информация о студентах:")
print(student1)
print()
print(student2)
print()

print("Информация о лекторах:")
print(lecturer1)
print()
print(lecturer2)
print()

print("Информация о проверяющих:")
print(reviewer1)
print()
print(reviewer2)
print()


# Функция для подсчета средней оценки за домашние задания по каждому студенту в рамках конкретного курса
def avg_hw_grade_by_course(students, course):
    total_avg = 0
    count_students = 0
    for student in students:
        if course in student.grades:
            total_avg += sum(student.grades[course]) / len(student.grades[course])
            count_students += 1
    if count_students == 0:
        return 0
    else:
        return total_avg / count_students


# Функция для подсчета средней оценки за лекции каждого лектора в рамках курса
def avg_lecture_grade_by_course(lecturers, course):
    total_avg = 0
    count_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.lecture_grades:
            total_avg += sum(lecturer.lecture_grades[course]) / len(lecturer.lecture_grades[course])
            count_lecturers += 1
    if count_lecturers == 0:
        return 0
    else:
        return total_avg / count_lecturers


# Вызов функций для подсчета средних оценок
course_name = 'Python'
print(
    f"Средняя оценка за домашние задания по курсу '{course_name}': {avg_hw_grade_by_course([student1, student2], course_name):.1f}")
print(
    f"Средняя оценка за лекции по курсу '{course_name}': {avg_lecture_grade_by_course([lecturer1, lecturer2], course_name):.1f}")



