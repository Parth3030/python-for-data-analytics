# Analyzing daily production output from CNC machine
daily_output = [145, 162, 138, 171, 155, 149, 168]  # pieces per day

total = 0
for pieces in daily_output:
    total += pieces

print(f"Weekly Production: {total:,} pieces")
print(f"Daily Average: {total//len(daily_output)} pieces/day")

# Slightly up: Flag low-output days
print("\nLow Output Days (<150 pieces):")
for i, pieces in enumerate(daily_output, start=1):
    if pieces < 150:
        print(f"  Day {i}: {pieces} pieces ")
