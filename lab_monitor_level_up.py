# Function with two parameters: concentration and the safety threshold
def check_safety(concentration, threshold):
    if concentration > threshold:
        return f"ALERT: {concentration} is above {threshold}!"
    else:
        return f"{concentration} is within safe limits."
    
# Data
samples = [0.5, 2.1, 1.8, 3.5, 0.9]
limit = 2.0

# Loop
for s in samples:
    # Pass TWO arguments into the function
    status = check_safety(s, limit)
    print(status)