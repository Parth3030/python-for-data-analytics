# --- Variable Cleanup ---

# 1. x -> total_revenue (or order_total)
old_x, total_revenue = 5000, 5000
print(f"Old: x | New: total_revenue | Value: {total_revenue}")

# 2. A -> branch_city
old_a, branch_city = 'Delhi', 'Delhi'
print(f"Old: A | New: branch_city | Value: {branch_city}")

# 3. temp -> is_active_status
old_temp, is_active_status = True, True
print(f"Old: temp | New: is_active_status | Value: {is_active_status}")

# 4. val1 -> tax_rate (or pi_value depending on context)
old_val1, tax_rate = 3.14, 3.14
print(f"Old: val1 | New: tax_rate | Value: {tax_rate}")

# 5. myVar -> product_category
old_myvar, product_category = 'Electronics', 'Electronics'
print(f"Old: myVar | New: product_category | Value: {product_category}")

# 6. n -> item_quantity
old_n, item_quantity = 42, 42
print(f"Old: n | New: item_quantity | Value: {item_quantity}")

# --- Final Verification ---
print("\nFinal clean variables ready for analysis:")
print(f"The {product_category} branch in {branch_city} sold {item_quantity} items.")
