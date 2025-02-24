from ProjectDemo1.DynamicArrays.Operations.add_product import AddProduct
from ProjectDemo1.DynamicArrays.Operations.update_product import UpdateProduct
from ProjectDemo1.DynamicArrays.Operations.delete_product import DeleteProduct
from ProjectDemo1.DynamicArrays.Operations.display_product import DisplayProduct
from ProjectDemo1.DynamicArrays.product_manager import ProductManager, Product

manager = ProductManager()

# Create instances of operation classes
add_op = AddProduct()
update_op = UpdateProduct()
delete_op = DeleteProduct()
display_op = DisplayProduct()

# Adding products
add_op.execute(manager, Product("PKG001", "Parcel to Toronto", 1, "Parcel"))
add_op.execute(manager, Product("PKG002", "Letter to Vancouver", 5, "Letter"))
add_op.execute(manager, Product("PKG003", "Package to Montreal", 2, "Package"))
add_op.execute(manager, Product("PKG004", "Express Document to Calgary", 3, "Express"))

print("Initial Shipments:")
display_op.execute(manager)

# Update product quantity for PKG002
update_op.execute(manager, "PKG002", new_quantity=4)
print("\nAfter Updating Shipment PKG002:")
display_op.execute(manager)

# Delete shipment PKG001
delete_op.execute(manager, "PKG001")
print("\nAfter Deleting Shipment PKG001:")
display_op.execute(manager)

