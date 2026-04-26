data = ' prod_001 | samsung mobile pro | RS.45,999.00 | in stock | delhi '

parts = data.split('|')

parts = [p.strip() for p in parts]

prod_id, product, price, status, city = parts

prod_id = prod_id.upper().replace('_', '-')

product = product.title()

clean_price = ''.join(ch for ch in price if ch.isdigit() or ch == '.')
clean_price = clean_price.lstrip('.')   # remove leading dot
price_float = float(clean_price)

status = status.title()

city = city.title()

print(f"Output: ID: {prod_id} | Product: {product} | Price: Rs.{price_float:,.1f} | Status: {status} | City: {city}")
