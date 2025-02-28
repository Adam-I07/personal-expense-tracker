import json_handling
import filter_expense_backend

class FilterExpense():
    def __init__(self):
        self.filter_expense_backend_instance = filter_expense_backend.FilterExpenseBackend()

    def filter_options(self):
        self.filter_expense_options()
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the filter you would like to invoke: ")
            if user_choice == "1":
                self.filter_by_date()
            elif user_choice == "2":
                pass
            elif user_choice == "3":
                pass
            elif user_choice == "4":
                pass
            elif user_choice == "5":
                pass
            elif user_choice == "6":
                return
            else:
                print("Invalid Input, try agian!")

    def filter_expense_options(self): 
        print("------------------------")
        print("Filter Expenses")
        print("------------------------")
        print("Options:")
        print("1. Filter by date")
        print("2. Filter by category")
        print("3. Filter by receipt availability")
        print("4. Filter by cost amount")
        print("5. Filter by description")
        print("6. Go Back")

    def filter_by_date(self):
        self.filter_by_date_options()
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the filter you would like to invoke: ")
            if user_choice == "1":
                self.filter_by_day()
            elif user_choice == "2":
                self.filter_by_month()
            elif user_choice == "3":
                self.filter_by_year()
            elif user_choice == "4":
                self.filter_expense_options()
                return
            else: 
                print("Invalid Input, try agian!")

    def filter_by_date_options(self):
        print("------------------------")
        print("Filter By Date")
        print("------------------------")
        print("Options:")
        print("1. Filter by Day")
        print("2. Filter by Month")
        print("3. Filter by Year")
        print("4. Go Back")
    
    def filter_by_day(self):
        print("------------------------")
        current_dates = self.filter_expense_backend_instance.get_dates()
        print("Options:")
        print("------------------------")
        num = 0
        nums = []
        for date in current_dates:
            num = num + 1
            nums.append(num)
            print(f"{num}. {date}")
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the day you would like to invoke: ")
            try:
                user_choice_int = int(user_choice)
                if user_choice_int in nums:
                    chosen_date = current_dates[user_choice_int-1]
                    print("------------------------")
                    self.filter_expense_backend_instance.create_day_table(chosen_date)
                    print("------------------------")
                    self.filter_by_date_options()
                    return
            except:
                print("Invalid Input, try again!")

    def filter_by_month(self):
        print("------------------------")
        current_months = self.filter_expense_backend_instance.get_months()
        current_months_name = self.filter_expense_backend_instance.get_month_name(current_months)
        print("Options:")
        print("------------------------")
        num = 0
        nums = []
        for month in current_months_name:
            num = num + 1
            nums.append(num)
            print(f"{num}. {month}")
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the month you would like to invoke: ")
            try:
                user_choice_int = int(user_choice)
                if user_choice_int in nums:
                    chosen_month = current_months[user_choice_int-1]
                    print("------------------------")
                    self.filter_expense_backend_instance.create_month_table(chosen_month)
                    print("------------------------")
                    self.filter_by_date_options()
                    return
            except:
                print("Invalid Input, try again!")

    def filter_by_year(self):
        print("------------------------")
        current_years = self.filter_expense_backend_instance.get_years()
        print("Options:")
        print("------------------------")
        num = 0
        nums = []
        for year in current_years:
            num = num + 1
            nums.append(num)
            print(f"{num}. {year}")
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the day you would like to invoke: ")
            try:
                user_choice_int = int(user_choice)
                if user_choice_int in nums:
                    chosen_year = current_years[user_choice_int-1]
                    print("------------------------")
                    self.filter_expense_backend_instance.create_year_table(chosen_year)
                    print("------------------------")
                    self.filter_by_date_options()
                    return
            except:
                print("Invalid Input, try again!")