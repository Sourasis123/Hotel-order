menu = {
    "Pizza": 50,
    "Pasta": 40,
    "Burger": 80,
    "Momo": 30,
    "Coffee": 70,
}

def add_item(menu, item, price):
    """Add a new item to the menu"""
    menu[item] = price

def display_menu(menu):
    """Display the menu"""
    print("\n--- JANA Restaurant Menu ---")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_order(menu):
    """Take customer order"""
    order_total = 0
    ordered_items = []

    while True:
        display_menu(menu)
        item = input("Enter the name of the item you want to order: ")
        if item in menu:
            order_total += menu[item]
            ordered_items.append(item)
            print(f"Item '{item}' has been added to your order.")
        else:
            print(f"Ordered item '{item}' is not available.")

        another_order = input("Do you want to add another item? (Yes/No): ")
        if another_order.lower() != "yes":
            break

    return order_total, ordered_items

# Add a new item to the menu
add_item(menu, "Sandwich", 60)

# Welcome message and taking order
print("Welcome to JANA Restaurant")

order_total, ordered_items = take_order(menu)

# Display the order summary
print("\n--- Your Order ---")
print(f"Items: {', '.join(ordered_items)}")
print(f"Total: ${order_total}")
