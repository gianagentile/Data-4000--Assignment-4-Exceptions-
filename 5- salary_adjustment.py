# get valid float input 
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# main program function 
def main():
    print("=== Employee Salary Adjustment Simulator ===")
    #get current 
    current_salary = get_valid_float("Enter current salary: ")
    # loop until valid 
    while True:
        try:
            percentage = get_valid_float("Enter asjustment percentage (0-100): ")
            #custom check 
            if percentage < 0:
                raise ValueError("Percentage cannot be negative.")
            if percentage > 100:
                print("Percentage cannot exceed 100. Please try again.")
                continue
            #calulate salary adjustment
            new_salary = current_salary * (1 + percentage / 100)
        except ValueError as e:
            print(f"Error: {e}")
        else:
            # run if no exceptions
            print(f"\nNew Salary: ${new_salary:.2f}")
            break

#run 
if __name__ == "__main__":
    main()  