#!/usr/bin/env python
# coding: utf-8

# In[2]:


                                                              #expense Tracker project
expenses = []
total = 0

while True:
    expense = input("Enter expense amount (or type 'bill' to finish): ")

    if expense.lower() == "bill":
        break

    expense = float(expense)
    expenses.append(expense)
    total += expense

print("\n----- Expense Summary -----")
print("Expenses:", expenses)
print("Total Spent:", total)
print("Number of Expenses:", len(expenses))


# In[ ]:




