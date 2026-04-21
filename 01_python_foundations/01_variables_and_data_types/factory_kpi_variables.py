# 1. Defining Factory KPI Variables
planned_production_target= 1200
actual_parts_produced= 1140
rejected_parts= 28
machine_downtime_minutes = 45
total_shift_minutes= 480
shift_supervisor_name = "Parth"

# 2. Calculating KPI Metrics
# Rejection Rate: Percentage of produced parts that failed quality checks
rejection_rate = (rejected_parts/ actual_parts_produced) * 100

# Productivity Pct: How much of the target was actually achieved
productivity_pct = (actual_parts_produced/ planned_production_target) * 100

# 3. Printing the KPI Dashboard
print("-" * 45)
print(f"{'FACTORY SHIFT KPI REPORT':^45}")
print("-" * 45)
print(f"Supervisor       : {shift_supervisor_name}")
print(f"Planned Target   : {planned_production_target} units")
print(f"Actual Produced  : {actual_parts_produced} units")
print(f"Downtime         : {machine_downtime_minutes} mins")
print("-" * 45)

# Formatting to 1 decimal place for professional reporting
print(f"Rejection Rate   : {rejection_rate:.1f}%")
print(f"Productivity     : {productivity_pct:.1f}%")
print("-" * 45)
