# 1. The messy input list
cities = ['Ahmedabad', 'ahmedabad', 'AHMEDABAD', 'Ahemdabad', 'mumbai', 'MUMBAI', 'Mumbai']

# We use list comprehension to apply .title() to every city first.
# This makes 'ahmedabad', 'AHMEDABAD', and 'Ahemdabad' all look like 'Ahmedabad' or 'Ahemdabad'.
standardized_cities = [city.title() for city in cities]

# Now we replace the misspelled version with the correct one.
cleaned_cities = [city.replace('Ahemdabad', 'Ahmedabad') for city in standardized_cities]

print(f"Output: {cleaned_cities}")
