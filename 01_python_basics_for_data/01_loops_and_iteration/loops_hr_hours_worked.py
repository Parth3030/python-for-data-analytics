# Tracking weekly hours worked by shop floor workers
weekly_hours = [48, 52, 45, 60, 47, 55, 42]  # hours per employee

total_hours = 0
for hours in weekly_hours:
    total_hours += hours

print(f"Team Size: {len(weekly_hours)} workers")
print(f"Total Hours Worked: {total_hours} hrs")
print(f"Average Hours/Worker: {total_hours//len(weekly_hours)} hrs")

# Slightly up: Flag overtime (>48 hrs/week)
overtime_threshold = 48
print(f"\nOvertime Alerts (>{overtime_threshold} hrs):")
for i, hours in enumerate(weekly_hours, start=1):
    if hours > overtime_threshold:
        extra = hours - overtime_threshold
        print(f"  Worker {i}: {hours} hrs (+{extra} hrs OT)")
