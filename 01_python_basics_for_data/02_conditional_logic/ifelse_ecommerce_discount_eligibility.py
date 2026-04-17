# Determining discount eligibility based on cart value + customer type
cart_values = [450, 2800, 12000, 850, 5500, 320, 18000]  # ₹ cart total
customer_types = ["new", "regular", "premium", "new", "regular", "new", "premium"]

print("Discount Eligibility Checker")
print("-" * 45)

for order, (cart, cust_type) in enumerate(zip(cart_values, customer_types), start=1):
    # Base discount by customer type
    if cust_type == "premium":
        base_discount = 15
    elif cust_type == "regular":
        base_discount = 10
    else:  # new
        base_discount = 5
    
    # Bonus discount for high cart value
    if cart >= 10000:
        bonus = 5
        reason = "+ High value cart"
    elif cart >= 2000:
        bonus = 2
        reason = "+ Medium cart"
    else:
        bonus = 0
        reason = ""
    
    total_discount = base_discount + bonus
    print(f"Order {order}: ₹{cart:,} ({cust_type}) → {total_discount}% off {reason}")
