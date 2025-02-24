from product_manager import Product, ProductManager

from add_product import AddProduct
from update_product import UpdateProduct
from delete_product import DeleteProduct
from display_product import DisplayProduct

class Product:
    def __init__(self, product_id, name, quantity, category):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.category = category

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Category: {self.category}"


class ProductManager:
    def __init__(self):
        # Initialize the dynamic array with a capacity of 1.
        self.array = [None]
        self.size = 0
        self.capacity = 1

    def _resize(self, new_capacity):
        """
        Resizes the internal array to the new_capacity.
        """
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity


if __name__ == "__main__":
    # Importing operation classes
    from add_product import AddProduct
    from update_product import UpdateProduct
    from delete_product import DeleteProduct
    from display_product import DisplayProduct

    # Create the product manager
    manager = ProductManager()

    # Create instances of each operation class
    add_op = AddProduct()
    update_op = UpdateProduct()
    delete_op = DeleteProduct()
    display_op = DisplayProduct()

    # Adding products
    add_op.execute(manager, Product("PKG001", "Parcel to Toronto", 1, "Parcel"))
    add_op.execute(manager, Product("PKG002", "Letter to Vancouver", 5, "Letter"))
    add_op.execute(manager, Product("PKG003", "Package to Montreal", 2, "Package"))
    add_op.execute(manager, Product("PKG004", "Express Document to Calgary", 3, "Express"))

    print("Initial Shipments:")
    display_op.execute(manager)

    # Update product quantity for PKG002
    update_op.execute(manager, "PKG002", new_quantity=4)
    print("\nAfter Updating Shipment PKG002:")
    display_op.execute(manager)

    # Delete shipment PKG001
    delete_op.execute(manager, "PKG001")
    print("\nAfter Deleting Shipment PKG001:")
    display_op.execute(manager)
