from product_manager import ProductManager

class DisplayProduct:
    def execute(self, manager: ProductManager) -> None:
        """
        Displays all products currently stored in the manager's dynamic array.
        """
        if manager.size == 0:
            print("The Warehouse is Empty")
        else:
            for i in range(manager.size):
                print(manager.array[i])
