# 1. Raw data as received from the CSV (all strings)
raw_quantity = '42'
raw_price = '3.14'
raw_is_active = 'True'
raw_date = '2024-01-15'
raw_product_id = 'PROD-001'
raw_stock_count = '0'

# 2. Analysis and Mapping
print("--- CSV Data Type Identification ---")

# We use type(var).__name__ to show the current type 'str'
# and then suggest the ideal conversion.

print(f"'{raw_quantity}' (quantity)  : {type(raw_quantity).__name__} -> should be int")
print(f"'{raw_price}' (price)        : {type(raw_price).__name__} -> should be float")
print(f"'{raw_is_active}' (active)   : {type(raw_is_active).__name__} -> should be bool")
print(f"'{raw_date}' (date)          : {type(raw_date).__name__} -> should be datetime")
print(f"'{raw_product_id}' (id)      : {type(raw_product_id).__name__} -> should be str (stay as is)")
print(f"'{raw_stock_count}' (stock)  : {type(raw_stock_count).__name__} -> should be int")

