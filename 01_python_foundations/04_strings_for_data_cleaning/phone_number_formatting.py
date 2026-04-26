phone_numbers = [
    '9876543210',
    '987 654 3210',
    '(987)654-3210',
    '91-9876543210',
    '98-76-54-32-10']

cleaned_numbers = []

for num in phone_numbers:
    
    digits = ""
    for ch in num:
        if ch.isdigit():
            digits += ch

    if len(digits) > 10:
        digits = digits[-10:]

    # Step 3: format
    formatted = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    
    cleaned_numbers.append(formatted)

# Print result
print("Output:")
for number in cleaned_numbers:
    print(number)
