# function to prompt usert to enter vaild number 
def get_valid_number(prompt, num_type):
    #loop until user enters a valid number
    while True:
        try:
            value = num_type(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#main function
def main(): 
    print("== Retail Sales Data Entry ==")
    #vaild interger for units sold 
    units_sold = get_valid_number("Enter the number of units sold: ", int)
    #valid float for unit price
    unit_price = get_valid_number("Enter the price per unit: ", float)
    # total revenue 
    total_revenue = units_sold * unit_price
    #display sales summary
    print("\n--- Sales Summary ---" )
    print(f"Units Sold: {units_sold}")
    print(f"Unit Price: ${unit_price:.2f}")
    print(f"Total Revenue: ${total_revenue:.2f}")

if __name__ == "__main__":
    main()