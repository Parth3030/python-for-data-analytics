# Machine downtime alert system - real factory OEE monitoring
machines = [("CNC-Lathe", 45, "Setup"), ("Milling", 120, "Breakdown"), ("CNC-Lathe", 25, "Material")]
for machine, downtime_min, reason in machines:
    if downtime_min > 60:                          # nested if
        print(f"CRITICAL ALERT: {machine} - {downtime_min} min downtime ({reason}) → Immediate maintenance needed")
    elif downtime_min > 30:
        print(f"WARNING: {machine} - {downtime_min} min downtime ({reason}) → Schedule check today")
    else:
        print(f"OK: {machine} - {downtime_min} min ({reason})")
