'''
FILE: revenue_calculator.py
CONTEXT: Monthly Financial Performance Report for CNC Manufacturing Unit
PURPOSE: Calculate total revenue and efficiency metrics (Weekly/Daily) 
         to assist in factory capacity planning.
'''

# --- INPUT DATA ---
parts_produced = 150       # Total quantity of CNC components manufactured this month
unit_price = 2000          # Selling price per component in Indian Rupees(INR)
weeks_in_month = 4         # Standard fiscal month duration for weekly averaging
working_days = 26          # Actual production days excluding Sundays and holidays


# Calculate the gross income before any tax or operational deductions
total_revenue = parts_produced * unit_price

# Determine the average income generated per fiscal week
weekly_average = total_revenue / weeks_in_month

# Determine the daily productivity value based on active factory days
daily_average = total_revenue / working_days

# --- OUTPUT GENERATION ---
# Printing the calculated metrics with comma formatting for financial clarity
print(f"Total Revenue: Rs.{total_revenue:,}")
print(f"Weekly Avg   : Rs.{weekly_average:,.0f}")
print(f"Daily Avg    : Rs.{daily_average:,.0f}")
