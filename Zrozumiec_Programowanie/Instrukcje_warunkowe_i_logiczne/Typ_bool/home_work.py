# Zadanie nr 1
# Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania.

# product1 = input("Podaj cene produktu pierwszego ")
# product2 = input("Podaj cene produktu drugiego ")
# product3 = input("Podaj cene produktu trzeciego ")
# print("Czy produkt pierwszy jest droższy od drugiego", product1 > product2)
# print("Czy produkt drugi jest droższy od pierwszego", product2 > product1)

# Zadanie nr 3
# Zmodyfikuj program obliczający wartość lokaty, tak aby dodatkowo wypisywał informacje, czy w
# planowanym okresie łączna wartość inwestycji wzrośnie o co najmniej 10%.

# Zastosuj wzór do obliczenia wartości lokaty, pobierając od użytkownika następujące dane:
# poczatkowa wartosc
# oprocentowanie
# czas trwania w latach
# Wzór to:
# wartość = wartość pocz. * (1 + procent / 100) ^ liczba lat

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

final_value = initial_value * (1 + percentage / 100) ** years
capital_growth = final_value - initial_value
capital_growth_percentage = (capital_growth / initial_value) * 100

print("Po", years, "latach Twoja lokata będzie warta", final_value)
print(f"Czy wartość Twojej lokaty wzrośnie w tym czasie o 10% lub więcej? {capital_growth_percentage >= 10}")
