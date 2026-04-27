# Monthly sales data for 8 sales representatives
# (rep_name, monthly_sales)
sales_reps = [
    ("Arjun Mehta", 95000),
    ("Sneha Gupta", 120000),
    ("Vikram Singh", 85000),
    ("Priya Iyer", 145000),
    ("Rohan Joshi", 110000),
    ("Anjali Nair", 75000),
    ("Karan Verma", 105000),
    ("Siddharth Rao", 92000)
]

target_amount = 100000
top_rep = sales_reps[0]  
reps_above_target = []
total_team_sales = 0

for name, sales in sales_reps:
    
    total_team_sales += sales
    
    
    if sales > top_rep[1]:
        top_rep = (name, sales)

        
    if sales > target_amount:
        reps_above_target.append(name)

print(f"Top Rep: {top_rep[0]} - Rs.{top_rep[1]:,}")
print(f"Above target: {len(reps_above_target)} reps ({", ".join(reps_above_target)})")
print(f"Team Total: Rs.{total_team_sales:,}")
