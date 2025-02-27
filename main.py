from colorama import Fore
import view_expense
import analysis
import add_expense
import edit_expense
import total_spending
import deleting_expense

class Start():
    def __init__(self):
        self.view_expense_instance = view_expense.ViewExpense()
        self.add_expense_instance = add_expense.AddExpense()
        self.edit_expense_instance = edit_expense.EditExpense()
        self.total_spending_instance = total_spending.TotalSpending()
        self.deleting_expense_instance = deleting_expense.DeletingExpense()

    def start_program(self):
            self.display_menu()
            while True:
                user_choice = input("Enter the numerical value assosciated with the option you would like to invoke: ")
                if user_choice == "1":
                    self.add_expense_instance.add_expense()
                    self.display_menu()
                elif user_choice == "2":
                    self.edit_expense_instance.edit_expense()
                    self.display_menu()
                elif user_choice == "3":
                    self.view_expense_instance.view_expenses()
                    self.display_menu()
                elif user_choice == "4":
                    self.deleting_expense_instance.delete_expense()
                    self.display_menu()
                elif user_choice == "5":
                    self.total_spending_instance.show_total()
                    self.display_menu()
                elif user_choice == "6":
                    print("------------------------")
                    print("Filter Expenses")
                    print("------------------------")
                elif user_choice == "7":
                    print("------------------------")
                    print("Analysis")
                    print("------------------------")
                elif user_choice == "8":
                    self.display_menu()
                elif user_choice == "9":
                    print("------------------------")
                    self.end_program()
                else:
                    print("------------------------")
                    print(Fore.RED + "Invalid input, you can only enter the numerical value assosciated with the 8 options! Try again." + Fore.WHITE)
                    print("------------------------")

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

    def end_program(self):
        print("Program Exited!")
        print("------------------------")
        exit()



if __name__ == "__main__":
    start_app = Start()
    start_app.start_program()