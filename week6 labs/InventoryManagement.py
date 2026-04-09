
itemID = 1000

def calculate_total_value(price,quantity):
    return price*quantity

def add_inventory_id():
    global itemID
    itemID += 1
    itemName= input("Enter the item name: ")
    quantity=int(input("Enter the quantity: "))
    price= int(input("Enter the price per item: $"))
    totalPrice=calculate_total_value(price,quantity)
    return totalPrice,itemName,quantity,price

def update_Inventory():
    userItemId=input("Enter the Item ID: ")
    if userItemId == itemID:
        newQuantity= int(input("Enter the new quanitity: "))
        newPrice=int((input("Enter the new price per item: ")))
        newTotalprice = calculate_total_value(price,quantity)

    else:
        print("Please enter a valid id!")

totalPrice, itemName, quantity, price = add_inventory_id()
# newPrice, newQuantity =update_Inventory()

print(f"Item :{itemName}")
print(f"Item Id: {itemID}")
print(f"Quanitity: {quantity}")
print(f"Price: ${price}")
print(f"Total Price: ${totalPrice}")
