class DeleteProduct:
    def __init__(self, head):
        self.head = head

    def delete(self, product_id):
        current = self.head
        prev = None
        while current:
            if current.product_id == product_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return self.head
            prev = current
            current = current.next
        return self.head
