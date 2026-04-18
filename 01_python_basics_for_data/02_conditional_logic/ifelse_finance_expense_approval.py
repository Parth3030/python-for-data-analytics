# Automating expense approval based on amount thresholds
expense_amounts = [850, 4500, 12000, 2500, 18000, 950, 35000]  # ₹ per expense

print("Expense Approval Workflow")
print("-" * 40)

for expense, amount in enumerate(expense_amounts, start=1):
    if amount <= 1000:
        approver = "Team Lead"
        timeline = "Same day"
    elif amount <= 10000:
        approver = "Department Head"
        timeline = "1-2 days"
    elif amount <= 25000:
        approver = "Finance Manager"
        timeline = "3-5 days"
    else:
        approver = "CFO"
        timeline = "1 week+"
    
    print(f"Expense {expense}: ₹{amount:,} → {approver}  ({timeline})")
