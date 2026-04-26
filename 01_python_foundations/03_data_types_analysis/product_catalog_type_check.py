# 1. Product Catalog Variables (one is intentionally wrong for the demo)
product_id = "PROD-99"       
price = 149.50               
stock = "25"


# We use isinstance(variable, type) to check the validity
id_check = "PASS (str)" if isinstance(product_id,str) else "FAIL"
price_check = "PASS (float)" if isinstance(price, float) else "FAIL"


if isinstance(stock, int):
    stock_check = "PASS (int)"
else:
    stock_check = f"FAIL (got {type(stock).__name__}, expected int)"

print("--- Product Catalog Validation ---")
print(f"product_id: {id_check}")
print(f"price     : {price_check}")
print(f"stock     : {stock_check}")
