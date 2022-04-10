# Zadanie nr 1
# W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów. Wyznacz średnią prędkość korzystając ze zmiennych.
srednia = 38 / 3
# print(f"Srednia wynosi = {srednia:.2f}")

# Zadanie nr 2
# Zakładając, że na lokatę wpłacono 1000 zł, a oprocentowanie wynosi 4% w skali roku, oblicz jaka będzie wartość lokaty po 5 latach.

# wartosc_pocz = 1000
# procent = 4
# liczba_lat = 5
#
# wartosc = wartosc_pocz * (1 + procent / 100) ** liczba_lat
# print(f'{wartosc:.2f} zł')

# Zadanie nr 3
# Oblicz jaką drogę pokonasz idąc do sklepu po czerwonych liniach i wypisz tyle myślników (-) jaki będzie wynik.
from math import sqrt
a = 9
b = 12
c1 = sqrt(a * a + b * b)
a = 9
b = 12
c2 = sqrt(a * a + b * b)

print('-' * (int(c1) + int(c2)))