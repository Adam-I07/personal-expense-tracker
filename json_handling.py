import json

class JsonHandling():
    def __init__(self):
        self.loaded_expenses = {}
        return

    def get_data(self):
        with open('expenses.json') as f:
            self.loaded_expenses = json.load(f)