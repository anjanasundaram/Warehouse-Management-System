from ProjectDemo1.LinkedList.Operations.add_product import AddProduct
from ProjectDemo1.LinkedList.Operations.delete_product import DeleteProduct
from ProjectDemo1.LinkedList.Operations.update_product import UpdateProduct
from ProjectDemo1.LinkedList.Operations.display_product import DisplayProduct

class ProductManager:
    def __init__(self):
        self.head = None

    def add_product(self, product_id, name, quantity, category):
        manager = AddProduct(self.head) #create instance for Add Product class
        self.head = manager.add(product_id, name, quantity, category)

    def delete_product(self, product_id):
        manager = DeleteProduct(self.head)
        self.head = manager.delete(product_id)

    def update_product(self, product_id, name=None, quantity=None, category=None):
        manager = UpdateProduct(self.head)
        self.head = manager.update(product_id, name, quantity, category)

    def display_products(self):
        manager = DisplayProduct(self.head)
        manager.display()
