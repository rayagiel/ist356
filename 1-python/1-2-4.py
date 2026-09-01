list = {}
while True:
    item = input("Enter grocery item: ")
    if item.lower() == "done":
        break
    quantity = int(input("Enter the quantity: "))
    list [item] = quantity
    print (f"Added {quantity} of {item} to the list.")

print("Grocery List:")
print (list)
    