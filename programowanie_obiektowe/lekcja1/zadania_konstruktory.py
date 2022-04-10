import random


class Product:
    def __init__(self, name, category, price):
        self.category = category
        self.name = name
        self.price = price

    def print_product(self):
        print(f'{self.name} {self.category} {self.price}')


class Apple:
    def __init__(self, type_name, size, price):
        self.type_name = type_name
        self.size = size
        self.price = price


class Potato:
    def __init__(self, type_name, price):
        self.type_name = type_name
        self.price = price


class Order:
    def __init__(self, first_name, last_name, products = None):
        self.first_name = first_name
        self.last_name = last_name
        if products is None:
            products = []
        self.products = products

        sum_price = 0
        for product in products:
            sum_price += product.price
        self.sum_price = sum_price

    def print_order(self):
        print(f"Imie zamawiajacego: {self.first_name} ,nazwisko: {self.last_name},")
        self.print_products()
        print(f"Suma zamówienia wynosi {self.sum_price}")

    def print_products(self):
        for product in self.products:
            product.print_product()

def create_order_with_random_products(first_name, last_name):
    products = []
    number_of_products = random.randint(1,10)
    for products_number in range (number_of_products):
        name = f"Product - {products_number}"
        category = "Bez kategori"
        price = random.randint(20, 600)
        products.append(Product(name, category, price))
    order = Order(first_name, last_name, products)
    return order


# if __name__ == '__main__':

    product1 = Product("kiełbasa", "wędlina", 20)
    product2 = Product("asus", "komputer", 3000)
    product3 = Product("monitor", "rtv", 1000)
    # product1.print_product()
    # product2.print_product()
    apple1 = Apple('golden', 20, 10)
    # products = [product1, product2 , product3]
    #
    # order1 = Order("grzegorz", "wesołowski", products,)
    # order1.print_order()

    order2 = create_order_with_random_products("grzegorz", "wesołowski")
    order2.print_order()