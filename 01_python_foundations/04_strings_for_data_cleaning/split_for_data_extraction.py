# 1. The raw CSV string
csv_line = 'Parth,Electronics,Laptop,3,45000,Mumbai'

# 2. Split the string into a list
# .split(',') looks for every comma and cuts the string there
data_list = csv_line.split(',')

# 3. Assign parts to named variables by their index
customer_name = data_list[0]
department    = data_list[1]
product       = data_list[2]
quantity      = data_list[3]
price         = data_list[4]
city          = data_list[5]

# 4. Output
print(f"Output: Customer: {customer_name} | Product: {product} | Price: {price} | City: {city}")
print(data_list)
