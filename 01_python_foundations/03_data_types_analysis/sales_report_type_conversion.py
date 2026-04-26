# 1. Raw messy data from the source
raw_sales = ['1200.5', '850', '2100.0', '450.75', '3200', '975.50']

# 2. Conversion: Turn every string into a float
sales_floats = [float(s) for s in raw_sales]

total_sales = sum(sales_floats)
max_sales = max(sales_floats)
min_sales = min(sales_floats)
avg_sales = total_sales / len(sales_floats)

print("--- SALES SUMMARY REPORT ---")
print(f"Total   : Rs.{total_sales:,.2f}")
print(f"Max     : Rs.{max_sales:,.2f}")
print(f"Min     : Rs.{min_sales:,.2f}")
print(f"Average : Rs.{avg_sales:,.2f}")

# Single line version for your expected output:
print(f"\nOutput: Total: Rs.{total_sales} | Max: Rs.{max_sales} | Min: Rs.{min_sales} | Avg: Rs.{avg_sales:.2f}")
