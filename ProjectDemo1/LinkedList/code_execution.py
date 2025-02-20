from product_manager import ProductManager

pm = ProductManager()

# Adding products
pm.add_product(101, "Laptop", 5, "Electronics")
pm.add_product(102, "Phone", 10, "Electronics")
pm.add_product(103, "Ipad", 15, "Electronics")
pm.add_product(104, "Printer", 20, "Electronics")
pm.add_product(105, "Monitor", 25, "Electronics")
pm.add_product(106, "Keyboard", 30, "Electronics")

# Displaying products
print("\nDisplaying products after adding.....")
print(".....................................")
pm.display_products()

# Updating a product
print("\nUpdating products.....")
print("......................")
pm.update_product(101, quantity=7)

print("\nDisplaying products after updating.....")
print(".......................................")
# Displaying after update
pm.display_products()

print("\nDeleting products.....")
print("......................")
# Deleting a product
pm.delete_product(102)

# Displaying after deletion
print("\nDeleting products after deletion.....")
print(".....................................")
pm.display_products()
