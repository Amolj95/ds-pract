class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to the inventory.")

    def check_quantity(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product.quantity
        return 0

    def make_purchase(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:
                    product.quantity -= quantity
                    total_cost = product.price * quantity
                    print(f"Purchase successful! Total cost: ${total_cost}")
                else:
                    print("Insufficient quantity in stock.")
                return
        print("Product not found in the inventory.")

# Example Usage
inventory = Inventory()

# Adding products to the inventory
product1 = Product("Laptop", 999.99, 10)
product2 = Product("Smartphone", 399.99, 20)
inventory.add_product(product1)
inventory.add_product(product2)

# Checking the quantity of a product
quantity_available = inventory.check_quantity("Laptop")
print(f"Available quantity of Laptop: {quantity_available}")

# Making a purchase
inventory.make_purchase("Laptop", 3)

# Checking the updated quantity after purchase
quantity_available_after_purchase = inventory.check_quantity("Laptop")
print(f"Available quantity of Laptop after purchase: {quantity_available_after_purchase}")
