# 1. Declaring revenue variables for each region with descriptive names
north_region_revenue = 450000  # Delhi
south_region_revenue = 380000  # Chennai
east_region_revenue = 290000   # Kolkata
west_region_revenue = 510000   # Mumbai

# 2. Calculating the total company revenue
total_company_revenue = (
    north_region_revenue + 
    south_region_revenue + 
    east_region_revenue + 
    west_region_revenue)

# 3. Printing the regional breakdown and the final total
print(f"North: Rs.{north_region_revenue} | "
      f"South: Rs.{south_region_revenue} | "
      f"East: Rs.{east_region_revenue} | "
      f"West: Rs.{west_region_revenue} | "
      f"Total: Rs.{total_company_revenue}")
