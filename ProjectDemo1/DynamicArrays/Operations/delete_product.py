from product_manager import ProductManager

class DeleteProduct:
    def execute(self, manager: ProductManager, product_id) -> None:
        """
        Deletes the product with the specified product_id from the manager's dynamic array.
        Performs array compaction and resizes if necessary.
        """
        index_to_delete = -1
        for i in range(manager.size):
            if manager.array[i].product_id == product_id:
                index_to_delete = i
                break

        if index_to_delete == -1:
            print("Product does not exist")
            return

        # Shift elements to fill the gap
        for i in range(index_to_delete, manager.size - 1):
            manager.array[i] = manager.array[i + 1]
        manager.array[manager.size - 1] = None
        manager.size -= 1

        # Resize the array if it's too sparse
        if manager.size <= manager.capacity // 4:
            manager._resize(manager.capacity // 2)
