# Case Study 5: ATM Transaction Sequence Simulation
balance = 5000.0
transactions = [
    ("DEPOSIT", 1500.0),
    ("WITHDRAW", 2000.0),
    ("WITHDRAW", 6000.0),
    ("DEPOSIT", 500.0),
    ("WITHDRAW", -100.0)
]
accepted = 0
rejected = 0

for transaction_type, amount in transactions:
    if amount <= 0:
        print("Rejected:", transaction_type, amount, "- amount must be positive")
        rejected += 1
    elif transaction_type == "DEPOSIT":
        balance += amount
        print("Accepted deposit:", amount, "| Balance:", balance)
        accepted += 1
    elif transaction_type == "WITHDRAW":
        if amount <= balance:
            balance -= amount
            print("Accepted withdrawal:", amount, "| Balance:", balance)
            accepted += 1
        else:
            print("Rejected withdrawal:", amount, "- insufficient balance")
            rejected += 1
    else:
        print("Rejected: unknown transaction type")
        rejected += 1

print("\nTRANSACTION SUMMARY")
print("Accepted:", accepted)
print("Rejected:", rejected)
print("Closing balance: Rs.", round(balance, 2))
