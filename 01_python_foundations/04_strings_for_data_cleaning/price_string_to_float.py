scraped_prices = ['Rs.1,299.00', 'Rs. 850', '2,499.99', 'INR 3200', '1199/-']

clean_prices = []

for p in scraped_prices:
    
    temp = p.replace('Rs.', '').replace('INR', '').replace(',', '').replace('/-', '')

    clean_str = "".join([char for char in temp if char.isdigit() or char=="."])
    
    
    clean_prices.append(float(clean_str))

total_sum = sum(clean_prices)

print(f"Output: {clean_prices} | Total: Rs.{total_sum:,.2f}")




