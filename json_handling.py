import json

class JsonHandling():
    def __init__(self):
        self.loaded_expenses = []
        return

    # get_all_expenses
    def get_data(self):
        try: 
            self.loaded_expenses.clear()
        except:
            pass
        with open('expenses.json') as f:
            self.loaded_expenses = json.load(f)
    
    #get_specific_expense
    def get_expense(self, expense_id):
        for expense in self.loaded_expenses:
            if expense['id'] == int(expense_id):
                return expense

    # get_existing_id
    def get_existing_id(self):
        self.get_data()
        ids = [expense['id'] for expense in self.loaded_expenses]
        return ids
    
    # delete_expenseget_amount_spend
    def get_costs(self):
        self.get_data()
        total_cost = []
        for expense in self.loaded_expenses:
            total_cost.append(expense['amount_spent'])
        return total_cost
    
    # delete_expense
    def delete_expense(self, id):
        self.get_data()
        for expense in self.loaded_expenses:
            if id == expense["id"]:
                self.loaded_expenses.remove(expense)
        self.save_all_expenses()
    
    # edit_expense
    def edit_expense(self, expense):
        self.get_data()
        id_to_change = expense["id"]
        for item in self.loaded_expenses:
            if id_to_change in item.values():
                item["date"] = expense["date"]
                item["category"] = expense["category"]
                item["has_receipt"] = expense["has_receipt"]
                item["description"] = expense["description"]
                item["amount_spent"] = expense["amount_spent"]
        self.save_all_expenses()
    
    def save_all_expenses(self):
        with open('expenses.json', "w") as f:
            json.dump(self.loaded_expenses, f, indent=4)

    # get_existing_dates
    def get_dates(self):
        self.get_data()
        dates = []
        for expense in self.loaded_expenses:
            dates.append(expense["date"])
        return dates

    # add_expense
    def add_expense(self, expense):
        self.get_data()
        new_id = self.get_next_available_id(self.loaded_expenses)
        expense['id'] = new_id
        self.loaded_expenses.append(expense)
        with open('expenses.json', "w") as f:
            json.dump(self.loaded_expenses, f, indent=4)

    # get_next_available_id
    def get_next_available_id(self, expenses):
        # Extract all the IDs from the expenses list
        ids = self.get_existing_id()
        # Sort the list of IDs
        ids.sort()
        # Check for the next available ID
        for i in range(1, len(ids)):
            if ids[0] != 1:
                return 1
            if ids[i] != ids[i-1] + 1:
                # Return the first missing ID
                return ids[i-1] + 1
        # If no gaps, return the next ID after the highest one
        return ids[-1] + 1