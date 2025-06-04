from products import Product  # Produktklasse importieren

class Store:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total = 0
        for product in self.products:
            if product.is_active():
                total += product.get_quantity()
        return total

    def get_all_products(self) -> list:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

if __name__ == "__main__":
    import products  # importiere die Produktklasse

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_active = best_buy.get_all_products()

    print(best_buy.get_total_quantity())             # z.B. 850 (100+500+250)
    print(best_buy.order([(products_active[0], 1), (products_active[1], 2)]))  # Bestellt 1x MacBook, 2x Bose Earbuds, gibt Gesamtpreis zurück
