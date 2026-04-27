order_record = ("ORD-2026-772", "Elena Rodriguez", "UltraTab Pro", 2, 850.00, "Chicago", "12-03-2026")

# Printing each field with its label
print(f"Order ID: {order_record[0]}")
print(f"Customer: {order_record[1]}")
print(f"Product: {order_record[2]}")
print(f"Qty: {order_record[3]}")
print(f"Unit Price: ${order_record[4]}")
print(f"City: {order_record[5]}")
print(f"Order Date: {order_record[6]}")

# Attempting to change the quantity
try:
    order_record[3] = 5
except TypeError as e:
    print(f"\nError: {e}")

# WHY TUPLES PROTECT DATA INTEGRITY:
# Tuples are "immutable," meaning once they are created, their contents cannot be 
# modified, added to, or removed. In a business context like an order record, 
# this prevents accidental data corruption or "silent bugs" where a piece of 
# finalized history is overwritten by another part of the program. 
# Using a tuple ensures that 'ORD-2026-772' stays exactly as it was logged.
