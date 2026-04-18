# Delivery delay categorization
deliveries = [("Client1", 2), ("Client2", 0), ("Client3", 7), ("Client4", 4)]  # client, delay_days
for client, delay in deliveries:
    if delay == 0:
        print(f"{client}: ON TIME")
    elif delay <= 3:
        print(f"{client}: MINOR DELAY")
    elif delay <= 7:
        print(f"{client}: MAJOR DELAY → Escalate")
    else:
        print(f"{client}: CRITICAL DELAY → Client notification required")
