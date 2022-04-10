# Zadanie nr 1
# Napisz funkcję, która podaną liczbę zamieni na zakres.
#
# Domyślnie przyjmujemy zakres jako +/- 10% podanej wartości.

def convert_number_to_range (number, range = 0.1):
    begin = number - number * range
    last = number + number * range
    return [begin, last]


converted_to_range = convert_number_to_range(100)
print(converted_to_range)

# Zadanie nr 2
# Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
#
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz listę już zapisanych osób, która domyślnie jest pusta.

# def add_student_to_school(name_str, participants = None):
#     if participants is None:
#         participants = []
#     name = name_str.split(",")
#     for name in name:
#         participants.append(name)
#     return participants
#
#
# students = "Grzegorz, Kina, Antos, Zoya"
#
# monday_course = add_student_to_school(students)
#
# print(monday_course)
# new_student = "Gracjan, Agata"
# tuesday_course = add_student_to_school(new_student, participants=monday_course)
#
# print(tuesday_course)


