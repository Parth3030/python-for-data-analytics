customer_ids = ['C001', 'C002', 'C003', 'C004', 'C005']

# Append: Adds to the very end
customer_ids.append('C006')

# Insert: Adds 'C000' at index 0 (the front)
customer_ids.insert(0, 'C000')

# Remove: Deletes the specific value 'C003'
customer_ids.remove('C003')

# Check Membership: Returns True or False
exists = 'C004' in customer_ids

# Count: Gets the current size
total_count = len(customer_ids)

print(f"After all ops: {customer_ids} | C004 exists: {exists} | Count: {total_count}")
