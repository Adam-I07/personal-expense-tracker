from colorama import Fore

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
                        print(Fore.RED + "Invalid day. Day must be between 1 and 31." + Fore.WHITE)
                        continue
                    # Validate month
                    if month < 1 or month > 12:
                        print(Fore.RED + "Invalid month. Month must be between 1 and 12." + Fore.WHITE)
                        continue
                    # Validate year
                    if year < 1900 or year > 2025:
                        print(Fore.RED + "Invalid year. Year must be between 1900 and 2025." + Fore.WHITE)
                        continue
                    # If all validations pass, return the date 
                    return input_date
                else:
                    print(Fore.RED + "Invalid format. Please use dd/mm/yyyy." + Fore.WHITE)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter numeric values for day, month, and year." + Fore.WHITE)

    def has_receipt_validation(self):
        while True:
            has_receipt = input("Do you have the receipt of the expense: yes/no: ")
            if has_receipt.lower() == "yes":
                return "yes"
            elif has_receipt.lower() == "no":
                return "no"
            else:
                print(Fore.RED + "Invalid input. Please enter yes or no." + Fore.WHITE)
    
    def amount_validation(self):
        while True:
            pounds_amount = input("Enter the pounds spent: ")
            pennys_amount = input("Enter the pennys spent: ")
            has_error = False

            int_check = self.check_if_int(pounds_amount, pennys_amount)
            
            if int_check is "Invalid":
                print(Fore.RED + "Invalid input. Please enter a numeric value." + Fore.WHITE)
                has_error = True
            
            if  len(pennys_amount) >= 3:
                print(Fore.RED + "Invalid input. Cannot enter more than 2 digits for pennys." + Fore.WHITE)
                has_error = True
            
            if has_error == False:
                return(f"£{pounds_amount}.{pennys_amount}")

    def amount_validation_filter(self):
        while True:
            pounds_amount = input("Enter the pounds to filter by: ")
            pennys_amount = input("Enter the pennys to filter by: ")
            
            has_error = False

            int_check = self.check_if_int(pounds_amount, pennys_amount)
            if int_check is "Invalid":
                print(Fore.RED + "Invalid input. Please enter a numeric value." + Fore.WHITE)
                has_error = True
            
            if  len(pennys_amount) >= 3:
                print(Fore.RED + "Invalid input. Cannot enter more than 2 digits for pennys." + Fore.WHITE)
                has_error = True
            
            if has_error == False:
                return(f"{pounds_amount}.{pennys_amount}")
            
    def check_if_int(self, pound_amount, penny_amount):
        try: 
            int(pound_amount)
            int(penny_amount)
            return pound_amount, penny_amount
        except:
            return "Invalid"

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
                print(Fore.RED + "Invalid choice. Please enter a numerical value between 1 and 9." + Fore.WHITE)

    def deletion_validation(self, id):
        while True:
            decision = input(f"Are you sure you would like to delete expense with the id: {id}, yes/no: ")
            if decision.lower() == 'yes':
                return 'yes'
            elif decision.lower() == 'no':
                return 'no'
            else:
                print(Fore.RED + "Invalid input, you can only enter yes or no" + Fore.WHITE)

