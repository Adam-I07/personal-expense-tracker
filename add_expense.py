from colorama import Fore

class AddExpense():
    def __init__(self):
        self.new_expense = {"id" : " ", "date" : " ", "category" : " ", "has_receipt" : " ", "description" : " ", "amount" : " "}
        pass
        
    def add_expense(self):
        self.add_expense_menu()
        while True:
            user_input = input("Enter the numerical value assosciated with the option you would like to invoke: ")
            if user_input == "1":
                self.create_expense()
            elif user_input == "2":
                pass
            elif user_input == "3":
                pass
            elif user_input == "4":
                pass
            elif user_input == "5":
                break
            else:
                print("------------------------")
                print(Fore.RED + "Invalid input! Try again!" + Fore.WHITE)
                print("------------------------")
    
    def go_back(self):
        return

    def create_expense(self):
        print("------------------------")
        print("Create Expense")
        print("------------------------")
        expense_date = self.date_validation()
        expense_category = input("Enter category of expense: ")
        expense_has_receipt = self.has_receipt_validation()
        expense_description = input("Enter description of receipt: ")
        expense_amount = self.amount_validation()
        self.new_expense["date"] = expense_date
        self.new_expense["category"] = expense_category
        self.new_expense["has_receipt"] = expense_has_receipt
        self.new_expense["description"] = expense_description
        self.new_expense["amount"] = expense_amount
        print(self.new_expense)
        

    def add_expense_menu(self):
        print("------------------------")
        print("Add Expense Menu")
        print("------------------------")
        print("Options:")
        print("1. Create Expense")
        print("2. Edit Expense")
        print("3. View Options")
        print("4. Submit Expense")
        print("5. Go Back")
        print("------------------------")
    
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
    


    