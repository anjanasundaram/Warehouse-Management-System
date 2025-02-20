class ProductNode:
    def __init__(self, product_id, name, quantity, category):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.category = category
        self.next = None