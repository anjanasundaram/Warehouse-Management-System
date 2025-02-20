from ProjectDemo1.LinkedList.product_node import ProductNode

class AddProduct:
    def __init__(self, head=None):
        self.head = head

    def add(self, product_id, name, quantity, category):
        new_node = ProductNode(product_id, name, quantity, category)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        return self.head