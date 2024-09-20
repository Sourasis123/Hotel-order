menu = {
    "Pizza":50,
    "Pasta":40,
    "Burgger":80,
    "Momo":30,
    "Coffe":70,
}
print("Welcom to JANA Restaurant")
print("Pizza: 50\nPasta: 40\nBurgger: 80\nMomo: 30\nCoffe: 70")

Order_total = 0

item_1 = input("Enter the name of item you want to order =")
if item_1 in menu:
    Order_total = menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print("Pleas order something else we can serve you")

another_order = input("Do you want to add another item? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2}is not avaialable")

print(f"The total amount of items is {Order_total}")