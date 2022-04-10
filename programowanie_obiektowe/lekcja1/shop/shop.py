from lekcja1.store.store import create_order_with_random_products



create_order_with_random_products("grzegorz","wesołowski")

if __name__ == '__main__':

    order = create_order_with_random_products("grzegorz", "wesołowski")

    order.print_order()