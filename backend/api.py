from fastapi import FastAPI, HTTPException 
import database_handling
import schema

api = FastAPI()
database_handling_instance = database_handling.DatabaseHander()

@api.post("/expense/add")
def add_expense(expense: schema.Expense):
    try:
        response = database_handling_instance.add_expense(expense)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Could not add expense")
    
@api.put("/expense/edit")
def edit_expense(expense: schema.Expense):
    try:
        response = database_handling_instance.edit_expense(expense)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail="Could not edit expense")

@api.delete("/expense/delete/{expense_id}")
def delete_expense(expense_id):
    try:
        response = database_handling_instance.delete_record("expenses", expense_id)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Could not delete expense: {e}")

@api.get("/expense/get/all")
def get_all_expenses():
    all_expenses = database_handling_instance.get_all_values("expenses")
    return all_expenses

@api.get("/expense/get/specific/{record_id}")
def get_specific_expense(record_id):
    expense = database_handling_instance.get_specific_record("expenses", int(record_id))
    return expense

@api.get("/expense/get/used/amount_spent")
def get_amount_spend():
    all_amount_spent = database_handling_instance.get_specfic_field("expenses", "amount_spent")
    one_array = []
    for amount_spent in all_amount_spent:
        for amount in amount_spent:
            one_array.append(amount)
    return one_array

@api.get("/expenses/get/used/id")
def get_existing_id():
    ids = database_handling_instance.get_specfic_field("expenses", "id")
    one_array = []
    for i in ids:
        for id in i:
            one_array.append(id)
    return one_array

@api.get("/expenses/get/used/dates")
def get_existing_dates():
    dates = database_handling_instance.get_specfic_field("expenses", "date")
    one_array = []
    for date in dates:
        for date_out_array in date:
            one_array.append(date_out_array)
    return one_array

@api.get("/expenses/get/next/id")
def get_next_available_id():
        ids = get_existing_id()
        ids.sort()
        for i in range(1, len(ids)):
            if ids[0] != 1:
                return 1
            if ids[1] != 2:
                return 2
            if ids[i] != ids[i-1] + 1:
                return ids[i-1] + 1
        return ids[-1] + 1
    

