python_age = 30

# info = "Python ma już prawie: " + str(python_age) + " lat!"

info = f"Python ma już prawie {python_age} lat!"

# calculation = f"Wynik działania 3 x 6 to {3 * 6}"

# name = "Mikołaj"
# hello = f"Nazywam się {name}"

distance = 35
time = 3
speed = distance / time

# print("Biegasz z prędkością średnią:", speed, "km/h!")

# print(f"Biegasz z prędkością średnią: {speed:.2f} km/h!")

# your_street = input("Na jakiej ulicy mieszkasz? ")

# print(f"Nazwa tej ulicy ma aż {len(your_street)} liter!")

# short = "Krótki napis"
# length = "Bardzo bardzo bardzo bardzo długi napis"
# print(short, "ma długość", len(short))
# print(length, "ma długość", len(length))

# big_letters = "mówię głośno!"
# print(big_letters.upper())

# small_letters = "CICHO I SPOKOJNIE"
# print(small_letters.lower())

# all_big = "RóżNe RoZmIaRy LiTeR".lower()
# print(all_big)

# name = input("Jak się nazywasz? ")
# print(f"Nazywasz się: {name.title()}")


# phone_number_with_space = '123 555 777'
# phone_number_with_dash = phone_number_with_space.replace(' ', '-')
# print(phone_number_with_dash)

phone_number = '(58)4612888'
phone_number = phone_number.replace('(', '')
phone_number = phone_number.replace(')', '')
print(phone_number)