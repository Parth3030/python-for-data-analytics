# 1. Input variables
parts_produced = 150
unit_price = 2000
weeks_in_month = 4
working_days = 26

# 2. Calculations (Stored in variables as requested)
total_revenue = parts_produced * unit_price
weekly_average = total_revenue / weeks_in_month
daily_average = total_revenue / working_days

# 3. Printing results with formatting
print(f"Total Revenue: Rs.{total_revenue:,}")
print(f"Weekly Avg   : Rs.{weekly_average:,.0f}")
print(f"Daily Avg    : Rs.{daily_average:,.0f}")
