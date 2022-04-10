# Zadanie nr 3
# Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej.
#
# Wypisz pierwszych 6 cyfr, a kolejne zastąp myślnikiem.

phone_num = input("Podaj numer telefonu: ")
correct_num = phone_num.replace('(', '')
good_number = correct_num.replace(')', '')
length_number = len(good_number)
secret_number = f"{good_number[:6]}{'_' * (length_number -6) }"
print("Urtyty numer to: ", secret_number)