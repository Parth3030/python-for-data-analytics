# The Structured Order ID
order_id = 'ORD-2026-MUM-00847'

# 1. Extraction using Slicing
# [0:3] starts at index 0 and stops BEFORE index 3
prefix = order_id[0:3]

# [4:8] starts at index 4 and stops BEFORE index 8 (the dash)
year = order_id[4:8]

# [9:12] starts at index 9 and stops BEFORE index 12
city = order_id[9:12]

# [-5:] starts at the 5th character from the end and goes to the very end
order_no = order_id[-5:]

# 2. Formatted Output
print(f"Output: Prefix: {prefix} | Year: {year} | City: {city} | Order No: {order_no}")
