weekly_sales = [45000.0, 62000.0, 21500.0, 89000.0, 54000.0, 33000.0, 90000.0]

total_revenue = sum(weekly_sales)
highest_day = max(weekly_sales)
lowest_day = min(weekly_sales)


print(f"Weekly Sales: {weekly_sales}")
print(f"Total: Rs.{total_revenue:,.1f} | Best: Rs.{highest_day:.1f} | Worst: Rs.{lowest_day:.1f}")
