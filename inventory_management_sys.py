# Inventory Management System

# Data Structures
inventory = []  # List to hold tuples of items
categories = set()  # Set to hold unique categories
inventory_dict = {}  # Dictionary to manage inventory by item names

# Function to display the menu
def display_menu():
    print("\nInventory Management System")
    print("-" * 30)
    print("1. Add an Item")
    print("2. View All Items")
    print("3. Search Item by Name")
    print("4. Update Item Quantity")
    print("5. View Items by Category")
    print("6. Exit")

# Add an item to the inventory
def add_item():
    item_name = input("Enter Item Name: ").strip()
    if item_name in inventory_dict:
        print("❗ This item already exists in the inventory.")
        return

    category = input("Enter Item Category: ").strip()
    price = float(input("Enter Item Price: "))
    quantity = int(input("Enter Item Quantity: "))

    # Create a tuple for the item
    item = (item_name, category, price, quantity)

    # Add to list and dictionary
    inventory.append(item)
    inventory_dict[item_name] = {"Category": category, "Price": price, "Quantity": quantity}

    # Add category to set
    categories.add(category)
    print("✅ Item added successfully!")

# View all items
def view_items():
    if not inventory:
        print("❗ Inventory is empty.")
        return

    print("\nAll Items:")
    print("-" * 50)
    for item in inventory:
        print(
            f"Name: {item[0]}, Category: {item[1]}, Price: {item[2]:.2f}, Quantity: {item[3]}"
        )

# Search for an item by name
def search_item():
    item_name = input("Enter Item Name to search: ").strip()
    if item_name in inventory_dict:
        print("\nItem Details:")
        for key, value in inventory_dict[item_name].items():
            print(f"{key}: {value}")
    else:
        print("❌ Item not found.")

# Update item quantity
def update_quantity():
    item_name = input("Enter Item Name to update quantity: ").strip()
    if item_name in inventory_dict:
        new_quantity = int(input("Enter New Quantity: "))
        inventory_dict[item_name]["Quantity"] = new_quantity

        # Update in the inventory list
        for i, item in enumerate(inventory):
            if item[0] == item_name:
                inventory[i] = (
                    item_name,
                    inventory_dict[item_name]["Category"],
                    inventory_dict[item_name]["Price"],
                    new_quantity,
                )
        print("✅ Quantity updated successfully!")
    else:
        print("❌ Item not found.")

# View items by category
def view_by_category():
    if not categories:
        print("❗ No categories available.")
        return

    print("\nAvailable Categories:", ", ".join(categories))
    selected_category = input("Enter a category to view items: ").strip()

    print(f"\nItems in Category: {selected_category}")
    print("-" * 50)
    found = False
    for item in inventory:
        if item[1] == selected_category:
            print(
                f"Name: {item[0]}, Price: {item[2]:.2f}, Quantity: {item[3]}"
            )
            found = True

    if not found:
        print("❌ No items found in this category.")

# Main function
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            search_item()
        elif choice == "4":
            update_quantity()
        elif choice == "5":
            view_by_category()
        elif choice == "6":
            print("👋 Exiting Inventory Management System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
