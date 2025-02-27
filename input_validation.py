class InputValidation():
    def __init__(self):
        pass

    def date_validation(self):
        while True:
            input_date = input("Enter date in the following format dd/mm/yyyy: ")
            try:
                split_date = input_date.split("/")
                if len(split_date) == 3:
                    day = int(split_date[0])
                    month = int(split_date[1])
                    year = int(split_date[2])
                    # Validate day
                    if day < 1 or day > 31:
                        print("Invalid day. Day must be between 1 and 31.")
                        continue
                    # Validate month
                    if month < 1 or month > 12:
                        print("Invalid month. Month must be between 1 and 12.")
                        continue
                    # Validate year
                    if year < 1900 or year > 2025:
                        print("Invalid year. Year must be between 1900 and 2025.")
                        continue
                    # If all validations pass, return the date 
                    return input_date
                else:
                    print("Invalid format. Please use dd/mm/yyyy.")
            except ValueError:
                print("Invalid input. Please enter numeric values for day, month, and year.")

    def has_receipt_validation(self):
        while True:
            has_receipt = input("Do you have the receipt of the expense: yes/no: ")
            if has_receipt.lower() == "yes":
                return "yes"
            elif has_receipt.lower() == "no":
                return "no"
            else:
                print("Invalid input. Please enter yes or no.")
    
    def amount_validation(self):
        while True:
            pounds_amount = input("Enter the pounds spent: ")
            pennys_amount = input("Enter the pennys spent: ")
            try: 
                int(pounds_amount)
                int(pennys_amount)
                return(f"£{pounds_amount}.{pennys_amount}")
            except:
                print("Invalid input. Please enter a numeric value.")

    def description_validation(self):
        while True:
            user_input = input("Enter description of receipt: ")
            if user_input:
                return user_input
            else:
                return "No Description Provided"
            
    def category_valdiation(self):
        print("------------------------")
        print("Select Category")
        print("1. Fuel Expense")
        print("2. Food Expense")
        print("3. Entertainment Expense")
        print("4. Accomodation Expense")
        print("5. Development and Training Expense")
        print("6. Work Equipment Expenses")
        print("7. Work Uniform Expenses")
        print("8. Client Expenses")
        print("9. Other Expense")

        while True:
            user_choice = input("Enter the numerical value assosciated category you would like to select: ")
            if user_choice == "1":
                print("------------------------")
                return "Fuel Expense"
            elif user_choice == "2":
                print("------------------------")
                return "Food Expense"
            elif user_choice == "3":
                print("------------------------")
                return "Entertainment Expense"
            elif user_choice == "4":
                print("------------------------")
                return "Accomodation Expense"
            elif user_choice == "5":
                print("------------------------")
                return "Development and Training Expense"
            elif user_choice == "6":
                print("------------------------")
                return "Work Equipment Expenses"
            elif user_choice == "7":
                print("------------------------")
                return "Work Uniform Expenses"
            elif user_choice == "8":
                print("------------------------")
                return "Client Expenses"
            elif user_choice == "9":
                print("------------------------")
                return "Other Expense"
            else:
                print("Invalid choice. Please enter a numerical value between 1 and 9.")