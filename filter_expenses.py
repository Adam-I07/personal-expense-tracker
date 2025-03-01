import filter_expense_backend
import input_validation

class FilterExpense():
    def __init__(self):
        self.filter_expense_backend_instance = filter_expense_backend.FilterExpenseBackend()
        self.input_validation_instance = input_validation.InputValidation()

    def filter_options(self):
        self.filter_expense_options()
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the filter you would like to invoke: ")
            if user_choice == "1":
                self.filter_by_date()
            elif user_choice == "2":
                self.filter_by_category()
            elif user_choice == "3":
                self.filter_by_receipt_availability()
            elif user_choice == "4":
                self.filter_by_cost()
            elif user_choice == "5":
                self.filter_by_description()
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
        print("4. Filter by amount spent")
        print("5. Filter by description")
        print("6. Go Back")

    # ---- Filter By Description ---- #
    def filter_by_description(self):
        while True:
            comparable_phrase = input("Enter singular phrase/word that you would like present in description: ")
            if comparable_phrase:
                self.filter_expense_backend_instance.check_word(comparable_phrase)
                print("----------------")
            else:
                print("Enter input!")

    # ---- Filter By Cost Amount ---- #
    def filter_by_cost(self):
        print("------------------------")
        amount = self.input_validation_instance.amount_validation_filter()
        self.filter_by_cost_options()
        while True:
            user_choice = input("Enter the number assosicated with the amount you would like to filter: ")
            try:
                if int(user_choice) == 1:
                    self.filter_expense_backend_instance.return_amount(int(user_choice), amount)
                    amount = self.input_validation_instance.amount_validation_filter()
                    self.filter_by_cost_options()
                elif int(user_choice) == 2:
                    self.filter_expense_backend_instance.return_amount(int(user_choice), amount)
                    amount = self.input_validation_instance.amount_validation_filter()
                    self.filter_by_cost_options()
                elif int(user_choice) == 3:
                    validity_of_amount = self.filter_expense_backend_instance.check_amount(amount)
                    if validity_of_amount == True:
                        self.filter_expense_backend_instance.return_amount(int(user_choice), amount)
                    else:
                        print(f"No matching values to £{amount}")
                    amount = self.input_validation_instance.amount_validation_filter()
                    self.filter_by_cost_options()
                elif int(user_choice) == 4:
                    self.filter_expense_options()
                    return
                else:
                    print("Invalid Input, Try Again!")
            
            except:
                print("Invalid Input, Try Again!")


    def filter_by_cost_options(self):
        print("------------------------")
        print("1. Get all costs higher than input")
        print("2. Get all costs lower than input")
        print("3. Get costs equal to input")
        print("4. Go Back")
        

    # ---- Filter By Receipt Availiability ---- #
    def filter_by_receipt_availability(self):
        self.filter_by_receipt_availability_options()
        while True:
            user_choice = input("Enter the number assosicated with the receipt availability you would like to filter: ")
            if int(user_choice) == 1:
                self.filter_expense_backend_instance.return_receipt_availability("Yes")
                self.filter_by_receipt_availability_options()
            elif int(user_choice) == 2:
                self.filter_expense_backend_instance.return_receipt_availability("No")
                self.filter_by_receipt_availability_options()
            elif int(user_choice) == 3:
                self.filter_expense_options()
                return
            else:
                print("Invalid Input, Try Again!")

    def filter_by_receipt_availability_options(self):
        print("------------------------")
        print("1. Has Receipt")
        print("2. Does Not Have Receipt")
        print("3. Go Back")
        

    # ---- Filter By Category ---- #

    def filter_by_category(self):
        filter_options = ["Fuel Expense", "Food Expense","Entertainment Expense", "Accomodation Expense", "Development and Training Expense", 
                          "Work Equipment Expenses", "Work Uniform Expenses", "Client Expenses", "Other Expense"] 
        self.filter_by_category_options(filter_options)
        while True:
            print("------------------------")
            user_choice = input("Enter the number assosicated with the category you would like to filter: ")
            if int(user_choice) > 0 and int(user_choice) < 10:
                self.filter_expense_backend_instance.return_category(int(user_choice)-1, filter_options)
                self.filter_by_category_options(filter_options)
            elif int(user_choice) == len(filter_options)+1:
                self.filter_expense_options()
                return
            else:
                print("Invalid Input, Select a valid category!")


    def filter_by_category_options(self, category_options):
        print("------------------------")
        num = 0
        for category in category_options:
            num += 1
            print(f"{num}. {category}")
        print(f"{num+1}. Go Back")
        
    # ---- Filter By Date ---- #

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