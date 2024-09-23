menu = {
    "Pizza": 50,
    "Pasta": 40,
    "Burger": 80,
    "Momo": 30,
    "Coffee": 70,
}

def add_item(menu, item, price):
    menu[item] = price

def display_menu(menu):
    for item, price in menu.items():
        print(f"{item}: {price}")


add_item(menu, "Sandwich", 60)

print("Welcome to JANA Restaurant")

# for item, price in menu.items():
#     print(f"{item}: {price}")

order_total = 0

item_1 = input("Enter the name of the item you want to order: ").strip().title()
if item_1 in menu:
    order_total = menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
    
    while True:
        another_order = input("Do you want to add another item? (Yes/No): ").strip().capitalize()
        if another_order == "Yes":
            item_2 = input("Enter the name of the second item: ").strip().title()
            if item_2 in menu:
                order_total += menu[item_2]
                print(f"Item '{item_2}' has been added to your order.")
            else:
                print(f"Ordered item '{item_2}' is not available.")
        else:
            break

    print(f"The total amount for your order is {order_total}")
else:
    print("Please order something else that we can serve you.")
