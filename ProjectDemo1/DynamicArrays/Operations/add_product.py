from product_manager import Product, ProductManager

class AddProduct:
    def execute(self, manager: ProductManager, product: Product) -> None:
        """
        Adds a product to the manager's dynamic array.
        Resizes the array if necessary.
        """
        if manager.size == manager.capacity:
            manager._resize(manager.capacity * 2)
        manager.array[manager.size] = product
        manager.size += 1
