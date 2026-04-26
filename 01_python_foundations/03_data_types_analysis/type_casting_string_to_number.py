# 1. Raw strings from CSV
raw_price = '2499.50'
raw_quantity = '12'
raw_discount_pct = '15'
raw_is_valid = 'True'

# 2. Type Casting
price = float(raw_price)
quantity = int(raw_quantity)
discount_pct = int(raw_discount_pct)

# The Trap: bool('False') is True because the string is not empty!
# Correct way to cast a string 'True'/'False' to a Boolean:
is_valid = raw_is_valid == 'True'

# 3. Calculation
# Logic: (Price * Quantity) - Discount
total_before_discount = price * quantity
discount_amount = total_before_discount * (discount_pct / 100)
final_total = total_before_discount - discount_amount

# 4. Output
if is_valid:
    print(f"Output: Final discounted total: Rs.{final_total}")
else:
    print("Data is invalid. Calculation skipped.")
