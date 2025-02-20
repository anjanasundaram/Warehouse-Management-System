class DisplayProduct:
    def __init__(self, head):
        self.head = head

    def display(self):
        if not self.head:
            return "Empty List"

        current = self.head
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Quantity: {current.quantity}, Category: {current.category}")
            current = current.next
