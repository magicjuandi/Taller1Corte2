class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.id not in self.products:
            self.products[product.id] = product
        else:
            print("Product already exists in inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            print("Product not found in inventory.")

    def update_product_quantity(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].quantity = quantity
        else:
            print("Product not found in inventory.")

    def list_products(self):
        for product_id, product in self.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

    def get_product_quantity(self, product_id):
        if product_id in self.products:
            return self.products[product_id].quantity
        else:
            print("Product not found in inventory.")
            return None

if __name__ == "__main__":
    inventory = Inventory()

    inventory.add_product(Product(1, "Camisa", 20.0, 50))
    inventory.add_product(Product(2, "Pantalón", 30.0, 30))
    print("Productos en el inventario:")
    
    inventory.list_products()
    inventory.update_product_quantity(1, 40)

    print("\nProductos en el inventario después de la actualización:")
    inventory.list_products()

    print("\nCantidad de Camisas en inventario:", inventory.get_product_quantity(1))

    inventory.remove_product(2)

    print("\nProductos en el inventario después de eliminar un producto:")
    inventory.list_products()
