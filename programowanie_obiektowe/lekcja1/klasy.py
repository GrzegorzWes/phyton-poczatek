import random


class Student:
    # Tak dziala domyslny konstruktor
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.promoted = False

class Grade:
    pass


class School:
    # Konstruktor nie musi "wprost" przypisywać przekazanych wartosci, można wykonać swoją logike
    def __init__(self, name, students):
        self.name = name
        if len(students) > 10:
            students = students[:10]
        self.students = students


def print_student(student):
    print(f"Student: {student.first_name} { student.last_name}, promoted: {student.promoted}")


def promote_student(student):
    student.promoted = True


# funkcja może zwracac obiekty
def create_school_with_students(school_name):
    numer_of_students = random.randint(1, 20)
    students =[]
    for student_number in range(numer_of_students):
        first_name = f"Student-{student_number}"
        last_name = "Smith"
        students.append(Student(first_name, last_name))

    school = School(school_name, students)
    return school


def run_example():
    school = create_school_with_students("Hogwart")
    print(school)
    for student in school.students:
        print_student(student)
    # student = Student("Ola", "Nowak")
    # student2 = Student("Jadzia", "Kubicka")
    # print_student(student)
    # print_student(student2)
    # promote_student(student2)
    # print_student(student2)


if __name__ == '__main__':
    run_example()