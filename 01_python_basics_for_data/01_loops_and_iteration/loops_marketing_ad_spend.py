# Tracking daily ad spend on Facebook campaigns
daily_spend = [1200, 1850, 950, 2400, 1600, 1100, 2100]  # ₹ per day

total_spend = 0
for spend in daily_spend:
    total_spend += spend

print(f"Weekly Ad Spend: ₹{total_spend:,}")
print(f"Daily Average: ₹{total_spend//len(daily_spend):,}")

# Slightly up: Flag high-spend days (>₹2000)
print(f"\nHigh Spend Days (>₹2,000):")
for i, spend in enumerate(daily_spend, start=1):
    if spend> 2000:
        print(f"  Day {i}: ₹{spend:,} → Review ROI")    
