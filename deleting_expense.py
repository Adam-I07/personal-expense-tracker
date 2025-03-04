import json_handling
import view_expense
import input_validation
from colorama import Fore

class DeletingExpense():
    def __init__(self):
        self.json_handling_instance = json_handling.JsonHandling()
        self.view_expense_instance = view_expense.ViewExpense()
        self.input_validation_instance = input_validation.InputValidation()

    def delete_expense(self):
        existing_id = self.json_handling_instance.get_existing_id()
        print("------------------------")
        print("Delete Expense")
        print("------------------------")
        self.view_expense_instance.view_expenses()
        self.expese_to_delete(existing_id)
        
    def expese_to_delete(self, existing_id):
        while True:
            input_decision = input("Enter the ID assosciated with the expense you would like to delete or enter 'b' to go back: ")
            try:
                if input_decision.lower() == 'b':
                    return
                elif int(input_decision) in existing_id:
                    confirmation_deletion = self.input_validation_instance.deletion_validation(input_decision)
                    if confirmation_deletion == 'yes':
                        self.json_handling_instance.delete_expense(int(input_decision))
                        return
                    else:
                        return
                else:
                    print(Fore.RED + "Invalid ID, input an existing ID from table!" + Fore.WHITE)
            except:
                print("Invalid ID, input existing ID from table!")

