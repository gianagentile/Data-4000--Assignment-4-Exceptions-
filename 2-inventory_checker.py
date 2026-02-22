# function to get valid integer 
def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# main program function 
def main():
    print("=== Inventory Quantity Checker ===")
    #get invenotry level 
    inventory_level = get_valid_integer("Enter the current inventory level: ")
    #get reorder theshold
    reorder_threshold = get_valid_integer("Enter minimum reorder threshold: ")
    try: 
        percentage = (inventory_level / reorder_threshold) * 100
        print(f"\nInventory level is at {percentage:.2f}% of the reorder threshold.")
        #check if reorder is needed
        if inventory_level < reorder_threshold:
            print(" Reorder Alert: Inventory level is below the minimum threshold.")
        else:
            print(" Inventory level is sufficient.")
    except ZeroDivisionError:
        print("Error: Reorder threshold cannot be zero.")
    
    # run program if correct 
if __name__ == "__main__":
    main()
