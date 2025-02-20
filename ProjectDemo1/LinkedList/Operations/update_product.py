class UpdateProduct:
    def __init__(self, head):
        self.head = head

    def update(self, product_id, name=None, quantity=None, category=None):
        current = self.head
        while current:
            if current.product_id == product_id:
                if name:
                    current.name = name
                if quantity is not None:
                    current.quantity = quantity
                if category:
                    current.category = category
                return self.head
            current = current.next
        return self.head
