from tabulate import tabulate
import json_handling

class AedvExpense():
    def __init__(self):
        self.current_expenses = {}
        self.json_handling_instance = json_handling.JsonHandling()
        
    
    def start_program(self):
        self.json_handling_instance.get_data()
        self.current_expenses = self.json_handling_instance.loaded_expenses
    
    def view_expenses(self):
        print("------------------------")
        print(tabulate(self.current_expenses,headers='keys', tablefmt='grid'))
        print("------------------------")

    def add_expense(self):
        pass
