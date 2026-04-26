# 1. Defining the raw numeric data
revenue = 1547832
growth_rate = 0.1847
avg_rating = 4.3678

# Revenue: Using , for thousands separators and .0f to remove decimals
# Note: Standard Python uses the International format (1,547,832)
f_revenue = f"Rs.{revenue:,}"

# Growth Rate: Using .2% multiplies by 100 and adds the '%' sign
f_growth = f"{growth_rate:.2%}"

# Rating: Using .1f rounds the float to one decimal place
f_rating = f"{avg_rating:.1f} stars"

print(f"Output: Revenue: {f_revenue} | "
      f"Growth: {f_growth} | "
      f"Rating: {f_rating}")


