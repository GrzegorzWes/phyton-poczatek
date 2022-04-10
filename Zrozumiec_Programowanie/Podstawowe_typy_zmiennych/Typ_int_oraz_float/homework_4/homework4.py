# Zadanie nr 1
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.

print("Jaka jest cana jabłek w:")
pirce_in_b = int(input("Biedronce: "))
price_in_l = int(input("Lidlu: "))
price_in_z = int(input("Zabce: "))
cheapest = min( pirce_in_b, price_in_l, price_in_z)
print("Najtańsze jabłka są po", cheapest)