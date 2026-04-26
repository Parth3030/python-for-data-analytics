# 1. Defining Zone item counts
zone_a = 847
zone_b = 392
zone_c = 1203

# 2. Calculations
total_items = zone_a+zone_b+zone_c

# Integer division (//) gives the base amount every zone can hold equally
items_per_zone_avg = total_items // 3

# Modulo (%) gives the "leftovers" that couldn't be distributed evenly
remainder = total_items % 3

# 3. Formatted Output
# Combining the results into a single line to match the expected output
print(f"Total: {total_items} | Per Zone (int division): {items_per_zone_avg} | Remainder: {remainder}")
