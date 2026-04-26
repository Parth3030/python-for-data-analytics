# --- EXAMPLE 1: Int to Float (The Calculation Shift) ---

total_sales = 10 
print(f"1. Count Before: {total_sales}  ({type(total_sales).__name__})")

total_sales = total_sales / 3  # Division automatically converts to float
print(f"   Count After : {total_sales:.2f} ({type(total_sales).__name__})")


# --- EXAMPLE 2: String to Float ---
unit_price = "1250.50" 
print(f"\n2. Price Before: {unit_price} ({type(unit_price).__name__})")

unit_price = float(unit_price)  # Convert string to float for math
print(f"   Price After : {unit_price} ({type(unit_price).__name__})")


# --- EXAMPLE 3: String to Boolean ---

is_delivered = "True"
print(f"\n3. Status Before: {is_delivered} ({type(is_delivered).__name__})")

# In real cleaning, we evaluate the string to get the boolean
is_delivered = (is_delivered == "True") 
print(f"   Status After : {is_delivered} ({type(is_delivered).__name__})")
