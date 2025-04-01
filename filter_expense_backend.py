import json_handling
from tabulate import tabulate

class FilterExpenseBackend():
    def __init__(self):
        self.json_handling_instance = json_handling.JsonHandling()

    def check_word(self, word):
        self.json_handling_instance.get_data()
        data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in data:
            description = expense["description"].lower()
            if word in description:
                return_info.append(expense)
        if return_info:
            self.create_table(return_info)
        else:
            print("Word not in any description")
            return

    def check_amount(self, amount):
        self.json_handling_instance.get_data()
        data = self.json_handling_instance.loaded_expenses
        amount_valid = False
        for expense in data:
            expense_amount = expense["amount_spent"]
            expense_amount_split = expense_amount.split("£")
            expense_amount = float(expense_amount_split[1])
            if expense_amount == float(amount):
                print("jere")
                amount_valid = True
                return amount_valid
        return False

    def return_amount(self, choice, amount):
        self.json_handling_instance.get_data()
        data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in data:
            expense_amount = expense["amount_spent"]
            expense_amount_split = expense_amount.split("£")
            expense_amount = float(expense_amount_split[1])
            if choice == 1:
                if expense_amount > float(amount):
                    return_info.append(expense)
            elif choice == 2:
                if expense_amount < float(amount):
                    return_info.append(expense)
            elif choice == 3:
                if expense_amount == float(amount):
                    return_info.append(expense)
            else:
                print("Invalid choice")
                return
            
        self.create_table(return_info)

    def return_receipt_availability(self, availability):
        self.json_handling_instance.get_data()
        data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in data:
            if expense["has_receipt"] == availability:
                return_info.append(expense)
        self.create_table(return_info)

    def return_category(self, category_to_return, filter_options):
        self.json_handling_instance.get_data()
        data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in data:
            if expense["category"] == filter_options[category_to_return]:
                return_info.append(expense)
        self.create_table(return_info)
    
    def get_dates(self):
        curret_dates = self.json_handling_instance.get_dates()
        filtered_dates = []
        for date in curret_dates:
            if date not in filtered_dates:
                filtered_dates.append(date)
        return filtered_dates
    
    def create_day_table(self, day):
        self.json_handling_instance.get_data()
        curret_data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in curret_data:
            if expense["date"] == day:
                return_info.append(expense)
        self.create_table(return_info)
        return
    
    def get_months(self):
        dates = self.json_handling_instance.get_dates()
        months = []
        for date in dates:
            split_date = date.split("-")
            if split_date[1] not in months:
                months.append(split_date[1])
        return months

    def get_years(self):
        dates = self.json_handling_instance.get_dates()
        years = []
        for date in dates:
            split_date = date.split("-")
            if split_date[2] not in years:
                years.append(split_date[2])
        return years
    
    def create_year_table(self, year_to_use):
        self.json_handling_instance.get_data()
        curret_data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in curret_data:
            split_date = expense["date"].split("-")
            split_year = split_date[2]
            if str(year_to_use) == split_year:
                return_info.append(expense)
        self.create_table(return_info)
        return

    def get_month_name(self, months_to_return):
        months = {"01" : "January", "02" : "February", "03" : "March", "04": "April", "05" : "May", "06": "June", "07": "July", "08": "August",  "09": "September", "10" : "October", "11" : "November", "12": "December"}
        months_name = []
        for month in months_to_return:
            if month in months:
                months_name.append(months[month])
        return months_name

    def create_month_table(self, month):
        self.json_handling_instance.get_data()
        curret_data = self.json_handling_instance.loaded_expenses
        return_info = []
        for expense in curret_data:
            split_date = expense["date"].split("-")
            split_month = split_date[1]
            if str(month) == split_month:
                return_info.append(expense)
        self.create_table(return_info)
        return

    def create_table(self, information):
        print(tabulate(information,headers = "keys", tablefmt="grid"))
