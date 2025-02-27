from tabulate import tabulate
import json_handling

class ViewExpense():
    def __init__(self):
        self.current_expenses = {}
        self.json_handling_instance = json_handling.JsonHandling()
    
    def view_expenses(self):
        self.json_handling_instance.get_data()
        self.current_expenses = self.json_handling_instance.loaded_expenses
        print("------------------------")
        print("View Expenses")
        print("------------------------")
        print(tabulate(self.current_expenses,headers='keys', tablefmt='grid'))
        print("------------------------")
