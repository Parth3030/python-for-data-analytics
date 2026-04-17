# Inventory Configuration
daily_stock = [240, 215, 198, 175, 160, 142, 128]
reorder_threshold = 150

print("Inventory Status Report")
print("-" * 35)

for day, current_level in enumerate(daily_stock, start=1):
    
    if current_level < reorder_threshold:
        status = "REORDER"
    else:
        status = "OK"

    print(f"Day {day}: {current_level} units {status}")

# Predictive Analytics
intervals = len(daily_stock) - 1
total_used = daily_stock[0] - daily_stock[-1]
avg_daily_use = total_used // intervals

if avg_daily_use > 0:
    days_until_stockout = daily_stock[-1] // avg_daily_use
    print("-" * 35)
    print(f"Projected stockout in ~{days_until_stockout} days")
