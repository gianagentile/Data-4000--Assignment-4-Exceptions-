# function to ask for cutomers age 
def get_customer_age():
    while True:
        try:
            # ask for age and convert it to an integer
            age = int(input("Please enter your age: "))
            if age <= 0:
                print("Age must be a positive number.")
                continue
            #return valid age 
            return age
        except ValueError:
            # non integr 
            print("Invalid input. Please enter a valid whole number.")

# main program funcion 
def main():
   print("=== Customer Age Verification ===")
   customer_age = get_customer_age()
   # ---stmulating name error ---
   eligabilty_age = 18 
   try: 
       if customer_age >= eligabilty_age:
           print("You are eligible for age restricted promotions.")
       else:
           print("Sorry, you are NOT eligible for age restricted promotions.")
   except NameError:
       print("Error detected: 'eligabilty_age' is not defined.")
       print("Fixing issue automatically...")
       # define missing variable
       eligabilty_age = 18  
       if customer_age >= eligabilty_age:
           print("You are eligible for age restricted promotions.")
       else:
           print("Sorry, you are NOT eligible for age restricted promotions.")
    
#runs 
if __name__ == "__main__":
    main()  