customer = 'Amit Shah'
product = 'CNC Part A'
qty = 25
unit_price = 1850.0
city = 'Ahmedabad'


subtotal = qty * unit_price
gst_amount = subtotal * 0.18
final_total = subtotal + gst_amount


print(f"Output: INVOICE | Customer: {customer} | Product: {product} | "
      f"Total: Rs.{subtotal:,.1f} | GST: Rs.{gst_amount:,.1f}")
