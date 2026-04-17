# Tracking defective parts per production batch
batch_defects = [3, 7, 2, 12, 5, 8, 4]  # defects per batch of 100 pieces

total_defects = 0
for defects in batch_defects:
    total_defects += defects

total_pieces = len(batch_defects) * 100
defect_rate = (total_defects / total_pieces) * 100

print(f"Total Batches: {len(batch_defects)}")
print(f"Total Defects: {total_defects} out of {total_pieces} pieces")
print(f"Overall Defect Rate: {defect_rate:.2f}%")

# Slightly up: Flag batches exceeding quality threshold
quality_threshold = 5  # max 5% defects acceptable
print(f"\nBatches Exceeding {quality_threshold}% Defect Threshold:")
for i, defects in enumerate(batch_defects, start=1):
    batch_rate = (defects / 100)* 100
    if batch_rate > quality_threshold:
        print(f"  Batch {i}: {batch_rate:.1f}% defects")
