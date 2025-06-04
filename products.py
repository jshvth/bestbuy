class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if not self.active:
            raise Exception("Cannot buy inactive product.")
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        total_price = self.price * quantity
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return total_price

if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))              # → 12500.0
    print(mac.buy(100))              # → 145000.0
    print(mac.is_active())           # → False

    print(bose.show())               # → "Bose QuietComfort Earbuds, Price: 250, Quantity: 450"
    print(mac.show())                # → "MacBook Air M2, Price: 1450, Quantity: 0"

    bose.set_quantity(1000)
    print(bose.show())               # → "Bose QuietComfort Earbuds, Price: 250, Quantity: 1000"
