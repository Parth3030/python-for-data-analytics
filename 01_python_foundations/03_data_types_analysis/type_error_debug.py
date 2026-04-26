monthly_sales = '45000'
bonus_percent = 10

# WHY IT FAILS: 
# 1. monthly_sales is a string ('str').
# 2. In Python, 'string' * int performs "Sequence Repetition" (repeating the text).
#    So, '45000' * 10 results in '45000450004500045000450004500045000450004500045000'.
# 3. Then, the code tries to divide that massive string by 100.
#    Python raises a TypeError because the '/' operator is not defined for strings.

# FIX: Convert the string to an integer before performing math
bonus = int(monthly_sales) * bonus_percent / 100

print(f"Output: Bonus amount: Rs.{bonus}")
