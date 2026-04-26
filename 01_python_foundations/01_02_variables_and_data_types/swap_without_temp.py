# 1. Initial output values
morning_shift_output = 85
evening_shift_output = 72

# Printing state before the swap
print(f"Before Swap: Morning = {morning_shift_output} | Evening = {evening_shift_output}")

# 2. The Pythonic Swap (Tuple Unpacking)
morning_shift_output, evening_shift_output = evening_shift_output, morning_shift_output

# 3. Printing state after the swap
print(f"After Swap : Morning = {morning_shift_output} | Evening = {evening_shift_output}")
