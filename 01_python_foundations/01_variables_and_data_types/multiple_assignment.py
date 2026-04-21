# 1. Multiple assignment to set the same base cost
zone_a_cost = zone_b_cost = zone_c_cost = 50

# 2. Applying individual surcharges
# Zone A gets Rs.20 extra
zone_a_cost += 20 

# Zone C gets Rs.35 extra
# (Zone B remains at the base cost of Rs.50)
zone_c_cost += 35

# 3. Printing the final costs
print(f"Zone A: Rs.{zone_a_cost}")
print(f"Zone B: Rs.{zone_b_cost}")
print(f"Zone C: Rs.{zone_c_cost}")
