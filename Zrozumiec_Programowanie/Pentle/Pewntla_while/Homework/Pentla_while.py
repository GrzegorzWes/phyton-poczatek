# Zadanie nr 1
# Pytaj użytkownika o liczbę tak długo aż poda liczbę parzystą lub przekroczy limit 10 prób.


# number = int(input("Podaj liczbę parzystą"))
# counter = 1
#
# while number % 2 !=0 and counter < 10:
#     number = int(input("Podaj liczbę parzystą"))
#     counter += 1
# print("Brawo!!!")

# Zadanie nr 2
# Wczytaj numer telefonu użytkownika i rozdziel go myślnikami (format XXX-XXX-XXX).

# tel_num = input("Podaj numer telefonu")
# tel_num = tel_num.replace('(', '')
# tel_num = tel_num.replace(')', '')
# formatted_number = ""
# number_index = 0
# while number_index< len(tel_num):
#     if number_index % 3 == 0 and number_index != 0:
#         formatted_number += "-"
#     formatted_number += tel_num[number_index]
#     number_index += 1
# print(formatted_number)

# Zadanie nr 3
# Poproś użytkownika o podanie ulubionych dań, rozdzielając każde z nich przecinkiem.
#
# Następnie wypisz każde z nich wraz z informacją, które miejsce zajmuje na jej/jego liście.
dishes = []
option = 'T'
while option == 'T':
    dish = input("Podaj ulubione danie: ")
    dishes.append(dish)
    option = input("Czy czesz dajej wprowadzać /T ? ")

index = 0
while index < len(dishes):
    print(f"[{index}] --> {dishes[index]}")
    index += 1