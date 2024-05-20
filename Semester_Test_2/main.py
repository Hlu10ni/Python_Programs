# Function to load inventory from a file into a list
def loadInventory():
    lst_inventory = []  # Initialize an empty list to store the inventory
    try:
        with open("inventory.txt", "r") as read_file:  # Open the file for reading
            for line in read_file:  # Iterate over each line in the file
                name, price, quantity = line.strip().split(",")  # Split the line by commas into name, price, and quantity
                lst_inventory.append([name, float(price), int(quantity)])  # Add the item as a list to the inventory list
    except FileNotFoundError:  # Handle the case where the file is not found
        print("Error: inventory.txt not found.")  # Print an error message
    return lst_inventory  # Return the loaded inventory list

# Function to save the current inventory list back to the file
def saveInventory(lst_inventory):
    with open("inventory.txt", "w") as write_file:  # Open the file for writing
        for item in lst_inventory:  # Iterate over each item in the inventory list
            write_file.write(f"{item[0]},{item[1]},{item[2]}\n")  # Write the item details to the file

# Function to display the menu options
def menu():
    print("\n1. Search for stationery")  # Print option to search for stationery
    print("2. Buy stationery (decrease quantity)")  # Print option to buy stationery
    print("3. Display all available stationery")  # Print option to display all available stationery
    print("0. Exit")  # Print option to exit

# Function to search for a specific item in the inventory
def search(lst_inventory, item_name):
    for inventory in lst_inventory:  # Iterate over each item in the inventory
        if item_name.capitalize() == inventory[0]:  # Check if the item name matches (case-insensitive)
            return f"Product Found:\n\t\tName: {inventory[0]}\n\t\tPrice: {inventory[1]}\n\t\tAvailable Quantity: {inventory[2]}"  # Return item details if found
    return "Item not available in the inventory"  # Return a message if the item is not found

# Function to buy a specified quantity of an item if available
def buy_stationery(lst_inventory, item_name, item_quantity, amount):
    for inventory in lst_inventory:  # Iterate over each item in the inventory
        if item_name.capitalize() == inventory[0]:  # Check if the item name matches (case-insensitive)
            total_amount = inventory[1] * item_quantity  # Calculate the total cost
            if item_quantity <= inventory[2] and amount >= total_amount:  # Check if the quantity is available and the amount is sufficient
                inventory[2] -= item_quantity  # Decrease the available quantity
                if inventory[2] == 0:  # Check if the item is out of stock
                    print("Out of Stock (The item is not available at the current moment)")  # Print out of stock message
                change = amount - total_amount  # Calculate the change
                return f"Purchase successful. Your change is {change:.2f}."  # Return success message with change
            elif item_quantity > inventory[2]:  # Check if the requested quantity is more than available
                return f"Insufficient quantity. Sorry we only have: {item_name} {inventory[2]}(s)"  # Return insufficient quantity message
            else:  # If the amount is insufficient
                return f"Insufficient amount: Your tendered amount is less than the total cost. The total cost is: R{total_amount:.2f}."  # Return insufficient amount message
    return "Item not available in the inventory"  # Return item not available message if not found


# Display All Available Stationery: Show the entire list in a readable format,
# with updated quantities reflecting any purchases.
def display_all_stationery(inventory_lst):
    print("UJ APB Van Schaik Bookshop Inventory")
    print("Name\t\t\tPrice\t\tQuantity")
    print("======================================")
    count = 0
    for inventory in inventory_lst:
        count = count + 1
        print(f"{count}. {inventory[0]}\t\t{inventory[1]}\t\t{inventory[2]}")

#display_all_stationery()

# Load the inventory from the file at the start
inventory_lst = loadInventory()

# Main loop to interact with the user
while True:
    print("\nWelcome to Van Schaik Bookshop")  # Print welcome message
    menu()  # Display the menu options

    option = input("Choose an option from above: 1-3 or 0 to exit: ")  # Prompt user for an option

    if option == "1":  # If the user chooses to search for stationery
        item_name = input("Enter the name of the item to search: ").capitalize()  # Prompt for the item name
        print(search(inventory_lst, item_name))  # Call search function and print the result
    elif option == "2":  # If the user chooses to buy stationery
        item_name = input("Enter the name of the item: ").capitalize()  # Prompt for the item name
        item_quantity = int(input("Enter the quantity of the item you want: "))  # Prompt for the quantity
        amount = float(input("Enter the tendering amount: "))  # Prompt for the tendering amount
        print(buy_stationery(inventory_lst, item_name, item_quantity, amount))  # Call buy function and print the result
    elif option == "3":  # If the user chooses to display all available stationery
        display_all_stationery(inventory_lst)  # Call display function
    elif option == "0":  # If the user chooses to exit
        saveInventory(inventory_lst)  # Save the inventory to the file
        print("Changes saved. Exiting...")  # Print exit message
        break  # Exit the loop
    else:  # If the user enters an invalid option
        print("Option is not available")  # Print error message
