# 01_variables_and_data_types.py

# --- 1. CONSTANTS (UPPER_CASE) ---
# Use for values that never change during the program execution.
GST_TAX_RATE = 0.18
MAX_WAREHOUSE_CAPACITY = 5000

# 2. COUNTERS
# Use descriptive names that imply a whole number (integer).
order_count = 150
returned_items_total = 12

# 3. BOOLEAN FLAGS 
# Names should pose a "Yes/No" question.
is_high_value_customer = True
has_inventory_shortage = False

# 4. CALCULATED METRICS
# Always include the unit (pct, amt, ratio) in the name.
conversion_rate_pct = 3.52
average_order_value_amt = 1250.75

# 5. RAW DATA FIELDS 
# Used for data imported directly from a database or CSV.
raw_customer_id = "CUS-9921"
raw_transaction_timestamp = "2026-03-27 10:30:00"

# 6. FORMATTED OUTPUT STRINGS 
# Helps distinguish between the data and the "pretty" version for printing.
f_total_revenue = f"Rs.{25000:,.2f}"
f_completion_status = f"Progress: {95:.2f}%"

# --- PRINTING THE GUIDE ---
print("--- ANALYTICS VARIABLE STYLE GUIDE ---")
print(f"{'Constant: TAX_RATE':<25} = {GST_TAX_RATE}")
print(f"{'Counter: Orders':<25} = {order_count}")
print(f"{'Flag: High Value?':<25} = {is_high_value_customer}")
print(f"{'Metric: Conversion':<25} = {conversion_rate_pct}%")
print(f"{'Raw Data: ID':<25} = {raw_customer_id}")
print(f"{'Formatted:':<25} = {f_total_revenue} | {f_completion_status}")
