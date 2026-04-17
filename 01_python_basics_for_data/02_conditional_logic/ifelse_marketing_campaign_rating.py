# Rating campaigns by ROI for budget allocation decisions
campaign_roi = [45, 120, -15, 85, 200, 30, 150]  # ROI percentage

print("Marketing Campaign Performance Rating")
print("-" * 45)

for campaign, roi in enumerate(campaign_roi, start=1):
    if roi >= 100:
        rating = "Excellent"
        action = "Increase budget"
    elif roi >= 50:
        rating = "Good"
        action = "Maintain budget"
    elif roi >= 0:
        rating = "Marginal"
        action = "Optimize before scaling"
    else:
        rating = "Losing Money"
        action = "Pause & review"
    
    print(f"Campaign {campaign}: {roi}% ROI | {rating} → {action}")
