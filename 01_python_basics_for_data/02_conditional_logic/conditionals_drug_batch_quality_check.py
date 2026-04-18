# Pharma batch quality check
batches = [("Batch-A", 98.5, 2), ("Batch-B", 95.2, 8), ("Batch-C", 99.1, 0)]  # name, purity_%, defects
for name, purity, defects in batches:
    if purity >= 98 and defects == 0:
        print(f"{name}: RELEASE TO MARKET")
    elif purity >= 95 and defects <= 5:
        print(f"{name}: HOLD FOR REVIEW")
    else:
        print(f"{name}: REJECT BATCH")
