from product_manager import ProductManager

class UpdateProduct:
    def execute(self, manager: ProductManager, product_id, new_name=None, new_quantity=None, new_category=None) -> None:
        """
        Updates the details of a product in the manager's dynamic array.
        """
        for i in range(manager.size):
            if manager.array[i].product_id == product_id:
                if new_name is not None:
                    manager.array[i].name = new_name
                if new_quantity is not None:
                    manager.array[i].quantity = new_quantity
                if new_category is not None:
                    manager.array[i].category = new_category
                return
        print("There is no product to update")
