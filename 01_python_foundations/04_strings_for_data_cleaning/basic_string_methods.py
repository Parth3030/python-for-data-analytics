raw_name = '  samsung-MOBILE  '

# Step 1: strip()
# Removes leading and trailing whitespace
step1 = raw_name.strip()
print(f"Step 1: '{step1}'")

# Step 2: lower()
# Converts everything to lowercase so formatting is consistent
step2 = step1.lower()
print(f"Step 2: '{step2}'")

# Step 3: replace()
# Swaps the hyphen for a clean space
step3 = step2.replace('-',' ')
print(f"Step 3: '{step3}'")

# Step 4: title()
# Capitalizes the first letter of every word
step4 = step3.title()
print(f"Step 4: '{step4}'")

# Final combined result
print(f"\nOutput: {step4}")
