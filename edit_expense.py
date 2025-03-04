from colorama import Fore
import json_handling
import view_expense
import input_validation

class EditExpense():
    def __init__(self):
        self.json_handling_instance = json_handling.JsonHandling()
        self.view_expense_instance = view_expense.ViewExpense()
        self.input_validation_instance = input_validation.InputValidation()

    def edit_expense(self):
        print("------------------------")
        print("Edit Expense")
        self.json_handling_instance.get_data()
        self.expense_ids = self.json_handling_instance.get_existing_id()
        self.view_expense_instance.view_expenses()
        while True:
            expense_to_edit = input("Enter the ID of the expense you would like to edit or 'b' to go back: ")
            try:
                if expense_to_edit.lower() == 'b':
                    return
                elif int(expense_to_edit) in self.expense_ids:
                    full_expense = self.json_handling_instance.get_expense(expense_to_edit)
                    expense_date = self.edit_date(full_expense['date'])
                    expense_category = self.edit_category(full_expense['category'])
                    expense_has_receipt = self.edit_has_receipt(full_expense['has_receipt'])
                    expense_description = self.edit_description(full_expense['description'])
                    expense_amount = self.edit_amount(full_expense['amount_spent'])
                    full_expense["date"] = expense_date
                    full_expense["category"] = expense_category
                    full_expense["has_receipt"] = expense_has_receipt
                    full_expense["description"] = expense_description
                    full_expense["amount_spent"] = expense_amount
                    self.confirm_edit_expense(full_expense)
                    return
                else:
                    print("Invalid ID, Try Again!")
            except:
                print("Invalid ID, Try Again!")

    def confirm_edit_expense(self, expense):
        while True:
            user_choice = input("Are you sure you would like to edit this expense, yes or no: ")
            if user_choice.lower() == 'yes':
                self.json_handling_instance.edit_expense(expense)
            elif user_choice.lower() == 'no':
                return
            else:
                print("Invalid input, you can only enter yes or no")
    
    def edit_description(self, description):
        while True:
            user_input = input(f"The current description is '{description}' would you like to edit it (y/n): ")
            if user_input.lower() == 'y':
                new_description = self.input_validation_instance.description_validation()
                return new_description
            elif user_input.lower() == 'n':
                return description
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)

    def edit_amount(self, amount):
        while True:
            user_input = input(f"The current amount of the expense is '{amount}' would you like to edit it (y/n): ")
            if user_input.lower() == 'y':
                new_amount = self.input_validation_instance.amount_validation()
                return new_amount
            elif user_input.lower() == 'n':
                return amount
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)

    def edit_has_receipt(self, receipt_status):
        while True:
            user_input = input(f"The current status of having the receipt is '{receipt_status}' would you like to edit it (y/n): ")
            if user_input.lower() == 'y':
                new_receipt_status = self.input_validation_instance.has_receipt_validation()
                return new_receipt_status
            elif user_input.lower() == 'n':
                return receipt_status
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)

    def edit_category(self, category):
        while True:
            user_input = input(f"The current category entered is '{category}' would you like to edit it (y/n): ")
            if user_input.lower() == 'y':
                new_category = self.input_validation_instance.category_valdiation()
                return new_category
            elif user_input.lower() == 'n':
                return category
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)
   
    def edit_date(self, date):
        while True:
            user_input = input(f"The current date entered is '{date}' would you like to edit it (y/n): ")
            if user_input.lower() == 'y':
                new_date = self.input_validation_instance.date_validation()
                return new_date
            elif user_input.lower() == 'n':
                return date
            else:
                print(Fore.RED + "Invalid input, try again!" + Fore.WHITE)

        
