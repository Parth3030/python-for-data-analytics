# 1. Defining the financial variables
base_price = 1299.99
gst_rate = 0.18

# 2. Calculating the final price
final_price_raw = base_price * (1 + gst_rate)

# 3. Applying precision using round()
final_price_rounded = round(final_price_raw, 2)

# 4. Output comparison
print(f"--- Financial Precision Report ---")
print(f"Without round : Rs.{final_price_raw}")
print(f"With round    : Rs.{final_price_rounded}")

# Analyst Tip: You can also use f-string formatting for display
print(f"F-string style: Rs.{final_price_raw:.2f}")
