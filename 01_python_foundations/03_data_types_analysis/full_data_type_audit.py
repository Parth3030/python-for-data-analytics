# 02_data_types_analysis.py

# 1. The Messy Record
age = 35.0                # Float (Should be Int)
revenue = "4500.75"       # String (Should be Float)
phone = 919876543210      # Int (Should be String)
is_active = "True"        # String (Should be Boolean)
zip_code = 380001         # Int (Should be String)
discount_rate = "0.10"    # String (Should be Float)



print(f"BEFORE: age={age} ({type(age).__name__})", end=" ")
age = int(age)
print(f"AFTER: age={age} ({type(age).__name__})")


print(f"BEFORE: revenue={revenue} ({type(revenue).__name__})", end=" ")
revenue = float(revenue)
print(f"AFTER: revenue={revenue} ({type(revenue).__name__})")


print(f"BEFORE: phone={phone} ({type(phone).__name__})", end=" ")
phone = str(phone)
print(f"AFTER: phone={phone} ({type(phone).__name__})")


print(f"BEFORE: is_active={is_active} ({type(is_active).__name__})", end=" ")
is_active = is_active == "True"
print(f"AFTER: is_active={is_active} ({type(is_active).__name__})")

print(f"BEFORE: zip_code={zip_code} ({type(zip_code).__name__})", end=" ")
zip_code = str(zip_code)
print(f"AFTER: zip_code={zip_code} ({type(zip_code).__name__})")

print(f"BEFORE: discount_rate={discount_rate} ({type(discount_rate).__name__})", end=" ")
discount_rate = float(discount_rate)
print(f"AFTER: discount_rate={discount_rate} ({type(discount_rate).__name__})")


print(f"\nOutput: age={age} (int) | phone='{phone}' (str) | revenue={revenue} (float) | active={is_active} (bool)")
