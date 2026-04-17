# Analyzing daily sales data using loops
daily_sales = [15000, 22000, 18500, 31000, 27500, 19000, 24000]

total = 0
for sale in daily_sales:
    total += sale

print(f"Weekly Total Revenue: ${total:,}")
print(f"Daily Average: ${total//len(daily_sales):,}")
