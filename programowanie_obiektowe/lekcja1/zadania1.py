
class Product:
    pass

class Order:
    pass

class Apple:
    pass

class Potato:
    pass

apple1 = Apple()
apple2 = Apple()
apple3 = Apple()

typA = Potato()
typB = Potato()
typC = Potato()

print("Rodzaj ziemniaków ", type(apple1))
print("Rodzaj ziemniaków ", type(apple2))
print("Rodzaj ziemniaków ", type(apple3))

zamowienie1 = Order()
zamowienie2 = Order()
zamowienie3 = Order()
zamowienie4 = Order()
zamowienie5 = Order()

all_orders = [zamowienie1, zamowienie2, zamowienie3, zamowienie4, zamowienie5]

slownik ={'goldstar': apple1,
          'golden': apple2,
          'champion': apple3
          }