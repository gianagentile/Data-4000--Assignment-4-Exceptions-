# function to prompt for valid flaot input 
def get_float(prompt):
    while True:
        try:
            # convert input to float 
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# main program function 
def main():
    print("=== Profit Margin Calculator ===")
    #loop indefinitely unril calculation works 
    while True:
        try: 
            #getting profit and reveune 
            profit = get_float("Enter profit; ")
            revenue = get_float("Enter revenue: ")
            # calculate profit margin
            ratio = profit / revenue
        except ZeroDivisionError:
            print("Revenue cannot be zero. Please try again.\n")
        else: 
            percent = ratio * 100
            print(f"\nProfit Margin: {percent:.2f}%")
            break

#runs 
if __name__ == "__main__":
    main()