# Operatory logiczne and/or/not (zadania)
# Napisz uproszczony kalkulator kredytowy.
#
# Celem kalkulatora jest sprawdzenie czy użytkownika stać na kredyt hipoteczny o podanych parametrach.
#
# Zapytaj użytkownika o:
# kwotę kredytu
# oprocentowanie kredytu
# wartość wkładu własnego
# czas kredytowania w latach
# przychód miesięczny
# sumę miesięcznych wydatków

# Oblicz ratę ze wzoru:
# (kwota kredytu * oprocentowanie / 100) / 12 + kwota kredytu / (liczba lat * 12)

# Oblicz dostępne środki jako:
# przychód - suma wydatków

# Oblicz wartość nieruchomości jako:
# wkład własny + kwota kredytu

print("Kalkulator kredytowy")
amount_of_credit = int(input("Podaj kwotę kredytu: "))
percentage = int(input("Oprocentowanie kredytu: "))
value_of_own_contribution = int(input("Podaj wartość wkładu własnego: "))
crediting_time = int(input("Podaj czas kredytowania: "))
monthly_income = int(input("Przychód miesięczny: "))
sum_of_monthly_expeneses = int(input("Podaj sumę miesięcznych wydatków: "))

loan_installment = (amount_of_credit * percentage) / 100 / 12 + amount_of_credit / (crediting_time * 12) # rata kredytu

available_funds = monthly_income - sum_of_monthly_expeneses # dostępne środki

value_of_property = value_of_own_contribution + amount_of_credit # wortość nieruchomości

percentage_participation = value_of_own_contribution /amount_of_credit * 100 # oblicznie procentowego wkładu własnego w stosunku do wartosci niechurmości

lower_value_of_own_contribution = value_of_own_contribution >= 10 and value_of_own_contribution <= 20
higher_value_of_own_contribution = value_of_own_contribution > 20

if higher_value_of_own_contribution:
    if available_funds > loan_installment + 1000:
        print("dostajesz kredyt")
elif lower_value_of_own_contribution:
    if available_funds > loan_installment + 2000:
        print("Dostajesz kredyt")
else:
    print("Nie dostaniesz kredytu")


