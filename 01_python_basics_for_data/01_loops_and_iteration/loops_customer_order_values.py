# Analyzing order values from recent customers
order_values = [2500, 8900, 1200, 15000, 3400, 7800, 4200]  # ₹ per order

total_revenue = 0
for order in order_values:
    total_revenue += order

print(f"Total Orders: {len(order_values)}")
print(f"Total Revenue: ₹{total_revenue:,}")
print(f"Average Order Value: ₹{total_revenue//len(order_values):,}")

# Slightly up: Segment customers by order value
print(f"\nCustomer Segments:")
for i, value in enumerate(order_values, start=1):
    if value>=10000:
        segment ="Premium"
    elif value>= 5000:
        segment ="Regular"
    else:
        segment = "New"
    print(f"  Customer {i}: ₹{value:,} → {segment}")
