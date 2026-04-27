products = [
    "Smartphone", "Laptop", "Tablet", "Headphones", "Smartwatch", 
    "Hoodie", "Jeans", "Sneakers", "T-Shirt", "Backpack"]

new_arrivals = products[:3]

clearance = products[-3:]

mid_range = products[3:7]

alternate_display = products[::2]

reversed_display = products[::-1]

print(f"New arrivals: {new_arrivals}")
print(f"Clearance: {clearance}")
print(f"Mid-range: {mid_range}")
print(f"Alternate display: {alternate_display}")
print(f"Reversed: {reversed_display}")
