from colorama import Fore
import json_handling
import input_validation

class AddExpense():
    def __init__(self):
        self.new_expense = {"id" : " ", "date" : " ", "category" : " ", "has_receipt" : " ", "description" : " ", "amount_spent" : " "}
        self.json_handling_instance = json_handling.JsonHandling()
        self.input_validation_instance = input_validation.InputValidation()
    
    def go_back(self):
        return

    def add_expense(self):
        print("------------------------")
        print("Add New Expense")
        print("------------------------")
        expense_date = self.input_validation_instance.date_validation()
        expense_category = self.input_validation_instance.category_valdiation()
        expense_has_receipt = self.input_validation_instance.has_receipt_validation()
        expense_description = self.input_validation_instance.description_validation()
        expense_amount = self.input_validation_instance.amount_validation()
        self.new_expense["date"] = expense_date
        self.new_expense["category"] = expense_category
        self.new_expense["has_receipt"] = expense_has_receipt
        self.new_expense["description"] = expense_description
        self.new_expense["amount_spent"] = expense_amount
        self.save_expense()
        
    def save_expense(self):
        while True:
            save_choice = input("Do you want to save this expense? (yes/no): ")
            if save_choice.lower() == "yes":
                self.json_handling_instance.add_expense(self.new_expense)
                break
            elif save_choice.lower() == "no":
                self.new_expense = {"id" : " ", "date" : " ", "category" : " ", "has_receipt" : " ", "description" : " ", "amount" : " "}
                return
            else:
                print(Fore.RED + "Invalid choice. Please enter yes or no." + Fore.WHITE)

    


    