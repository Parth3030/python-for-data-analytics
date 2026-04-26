# 1. Defining the Sales Transaction Data
order_id= "ORD-2024-001"
customer_name= "Parth"
product_name= "Mechanical Keyboard"
quantity= 2
unit_price= 4500.0
discount_percent= 10.0
city= "Ahmedabad"
is_online_order = True

# 2. Calculating the final total (for a complete receipt)
total_before_discount = quantity * unit_price
discount_amount = total_before_discount * (discount_percent / 100)
final_total = total_before_discount - discount_amount

# 3. Printing the Formatted Receipt
print("-" * 40)
print(f"{'ORDER RECEIPT':^40}")  
print("-" * 40)

# Using left padding (:<15) to align the labels
print(f"{'Order ID':<15}: {order_id}")
print(f"{'Customer':<15}: {customer_name}")
print(f"{'City':<15}: {city}")
print(f"{'Product':<15}: {product_name}")
print(f"{'Quantity':<15}: {quantity}")
print(f"{'Unit Price':<15}: Rs.{unit_price:,.2f}")
print(f"{'Discount':<15}: {discount_percent}%")
print(f"{'Channel':<15}: {'Online' if is_online_order else 'In-Store'}")

print("-" * 40)
print(f"{'TOTAL AMOUNT':<15}: Rs.{final_total:,.2f}")
print("-" * 40)
