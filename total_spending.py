import json_handling
from tabulate import tabulate

class TotalSpending():
    def __init__(self):
        self.json_handling_instance = json_handling.JsonHandling()

    def show_total(self):
        costs = self.json_handling_instance.get_costs()
        total_cost = self.calculate_total(costs)
        print("------------------------")
        print("Total Spending")
        print("------------------------")
        data = [{"Toal Spending:" : f"£{total_cost}"}]
        output_table = tabulate(data,headers = "keys", tablefmt="grid")
        print(output_table)

    def calculate_total(self, costs):
        price = []
        for amount in costs:
            amount_split = amount.split("£")
            amount_float = float(amount_split[1])
            price.append(amount_float)
        return sum(price)
        