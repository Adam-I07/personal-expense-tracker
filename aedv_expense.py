from tabulate import tabulate
import json_handling

class AedvExpense():
    def __init__(self):
        self.current_expenses = {}
        self.json_handling_instance = json_handling.JsonHandling()
        
    
    def start_program(self):
        print("1")
        self.json_handling_instance.get_data()
        print("here")
        self.current_expenses = self.json_handling_instance.loaded_expenses
        print(self.current_expenses)
        return
    
    def display_expenses(self):
        print("------------------------")
        print(tabulate(self.current_expenses,headers='keys', tablefmt='grid'))
        print("------------------------")

    def view_expense(self):
        return
