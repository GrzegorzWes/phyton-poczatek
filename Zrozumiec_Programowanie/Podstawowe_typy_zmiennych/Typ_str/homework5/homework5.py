# Zadanie nr 1
# Dostosuj program liczący wartość lokaty, tak aby wyświetlał ją z dokładnością do groszy (dwóch cyfr po przecinku).

# Zastosuj wzór do obliczenia wartości lokaty, pobierając od użytkownika następujące dane:
# poczatkowa wartosc
# oprocentowanie
# czas trwania w latach
# Wzór to:
# wartość = wartość pocz. * (1 + procent / 100) ^ liczba lat


# Zadanie nr 2
# Zapytaj użytkownika o imię i wypisz ile liter zawiera.

# imie = input("Podaj imię: ")
# print("Twoje imie zawiera", len(imie), "znaków")


# Zadanie nr 3
# Zapytaj użytkownika gdzie mieszka i wypisz odpowiedź, np. "Jak miło, że mieszkasz w Gdańsku".

# city = input("Gdzie mieszkasz: ")
# print("Jak miło, że mieszkasz w", city.title())


# Zadanie nr 4
# Wyobraź sobie, że przetwarzasz dane dotyczące samochodów.
#
# Numery tablic rejestracyjnych zostały jednak zapisane w niespójny sposób:

ford = "ab100100"
audi = "EEE 123123"
citroen = "Zk-300300"
honda = "AB210210"

# def replace_plate (plate):
#     plate = plate.upper
#     plate.replace(' ', '')
#     plate.replace('-','')
#     return plate

good_plateF = ford.upper()
good_plateA = audi.replace(' ', '')
good_plateC = citroen.replace('-', '').upper()
print(good_plateC)