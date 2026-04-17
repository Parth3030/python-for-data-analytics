# Employee performance rating system
employees = [("Operator1", 92, 3), ("Operator2", 65, 8), ("Operator3", 85, 1)]  # name, attendance_%, warnings
for name, attendance, warnings in employees:
    if attendance >= 90 and warnings == 0:
        print(f"{name}: EXCELLENT → Bonus eligible")
    elif attendance >= 75 and warnings <= 3:
        print(f"{name}: GOOD → Needs minor improvement")
    else:
        print(f"{name}: NEEDS ATTENTION → Performance review required")
