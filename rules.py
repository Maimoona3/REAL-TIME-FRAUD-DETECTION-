def check_rules(transaction):

    risk = 0.0

    # Rule 1: High amount
    if transaction.amount > 50000:
        risk += 0.5

    # Rule 2: Unknown location
    if transaction.location.lower() != "home":
        risk += 0.3

    # Rule 3: Suspicious device
    if transaction.device.lower() == "unknown":
        risk += 0.2

    return risk