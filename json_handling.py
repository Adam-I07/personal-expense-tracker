import json

class JsonHandling():
    def __init__(self):
        self.loaded_expenses = []
        return

    def get_data(self):
        try: 
            self.loaded_expenses.clear()
        except:
            pass
        with open('expenses.json') as f:
            self.loaded_expenses = json.load(f)

    def get_expense(self, expense_id):
        for expense in self.loaded_expenses:
            if expense['id'] == int(expense_id):
                return expense

    def get_existing_id(self):
        self.get_data()
        ids = [expense['id'] for expense in self.loaded_expenses]
        return ids
    
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

    def add_expense(self, expense):
        self.get_data()
        new_id = self.get_next_available_id(self.loaded_expenses)
        expense['id'] = new_id
        self.loaded_expenses.append(expense)
        print(self.loaded_expenses)
        with open('expenses.json', "w") as f:
            json.dump(self.loaded_expenses, f, indent=4)

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