from colorama import Fore
import aedv_expense
import analysis
import add_expense

class Start():
    def __init__(self):
        self.aedv_instance = aedv_expense.AedvExpense()
        self.add_expense_instance = add_expense.AddExpense()

    def start_program(self):
        self.aedv_instance.start_program()
        self.load_menu()

    def display_menu(self):
        print("------------------------")
        print("Personal Expense Tracker")
        print("------------------------")
        print("Options:")
        print("1. Add Expense")
        print("2. Edit Expenses")
        print("3. View Expenses")
        print("4. Delete Expense")
        print("5. Total Spending")
        print("6. Filter Expenses")
        print("7. Analysis")
        print("8. View Options")
        print("9. Exit")
        print("------------------------")

    def load_menu(self):
        self.display_menu()
        while True:
            user_choice = input("Enter the numerical value assosciated with the option you would like to invoke: ")
            if user_choice == "1":
                self.add_expense_instance.add_expense()
                self.display_menu()
            elif user_choice == "2":
                print("------------------------")
                print("Edit Expenses")
                print("------------------------")
            elif user_choice == "3":
                print("------------------------")
                print("View Expenses")
                self.aedv_instance.view_expenses()
            elif user_choice == "4":
                print("------------------------")
                print("Delete Expense")
                print("------------------------")
            elif user_choice == "5":
                print("------------------------")
                print("Total Spending")
                print("------------------------")
            elif user_choice == "6":
                print("------------------------")
                print("Filter Expenses")
                print("------------------------")
            elif user_choice == "7":
                print("------------------------")
                print("Analysis")
                print("------------------------")
            elif user_choice == "8":
                self.load_menu()
            elif user_choice == "9":
                print("------------------------")
                self.end_program()
            else:
                print("------------------------")
                print(Fore.RED + "Invalid input, you can only enter the numerical value assosciated with the 8 options! Try again." + Fore.WHITE)
                print("------------------------")

    def end_program(self):
        print("Program Exited!")
        print("------------------------")
        exit()



if __name__ == "__main__":
    start_app = Start()
    start_app.start_program()