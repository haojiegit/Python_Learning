def check_safety(concentration):
    if concentration > 2.0:
        return "Alert: High concentration!"
    else:
        return "Level Nominal"
    
samples = [0.5, 2.1, 1.8, 3.5, 0.9]

for s in samples:
    status = check_safety(s)
    print(f"Concentration: {s} - {status}")