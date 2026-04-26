# 1. Defining Boolean Flags
is_paid = True
is_shipped = False
is_returned = False
is_premium_customer = False
is_bulk_order = True


payment_status = "Payment received" if is_paid else "Payment pending"
shipping_status = "Shipped" if is_shipped else "Not yet shipped"
customer_tier = "Premium customer" if is_premium_customer else "Standard customer"
order_type = "Bulk order" if is_bulk_order else "Retail order"

# 3. Output
print("--- ORDER STATUS SUMMARY ---")
print(f"Status   : {payment_status}. {shipping_status}.")
print(f"Details  : {customer_tier} | {order_type}")

# Analyst Tip: You can also print the raw booleans for a quick audit
print(f"Raw Audit: Paid={is_paid}, Shipped={is_shipped}, Return={is_returned}")
