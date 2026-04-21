"""
FILE: single_and_multi-line_comments.py
AUTHOR: Parth (Data Analyst)
DATE: 28-03-2026
PURPOSE: This script calculates the net profit margin for specific products
         to evaluate business health and markup strategies.
"""

# 1. Initialize product data
product_name = "Laptop"
selling_price = 85000.0  # Revenue per unit
cost_price = 65000.0     # Production/Acquisition cost

# 2. Calculate the raw profit (Price - Cost)
profit = selling_price - cost_price

# 3. Calculate the Profit Margin percentage
# Formula: (Profit / Selling Price) * 100
margin_percentage = (profit / selling_price) * 100

# 4. Generate the final performance output
# We use :.1f to round to one decimal place
print(f"Profit Margin for {product_name}: {margin_percentage:.1f}%") # Good margin for electronics
