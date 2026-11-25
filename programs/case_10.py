# Case Study 10: Campus Festival Financial Audit
participants = [
    ("REG101", 300.0),
    ("REG102", 300.0),
    ("REG103", 300.0),
    ("REG102", 300.0),  # Duplicate registration ID
    ("REG104", 300.0)
]
sponsorships = [5000.0, 3000.0]
expenses = [
    ("Venue", 4000.0),
    ("Sound", 2500.0),
    ("Food", 3500.0),
    ("Transport", 1000.0)
]

seen_ids = []
duplicates = []
registration_income = 0.0

for registration_id, fee in participants:
    if registration_id in seen_ids:
        duplicates.append(registration_id)
    else:
        seen_ids.append(registration_id)
        if fee >= 0:
            registration_income += fee

sponsorship_total = sum(sponsorships)
expense_total = 0.0
for expense_name, amount in expenses:
    expense_total += amount

total_income = registration_income + sponsorship_total
balance = total_income - expense_total

print("CAMPUS FESTIVAL FINANCIAL AUDIT")
print("Unique registrations:", len(seen_ids))
print("Duplicate IDs:", duplicates if duplicates else "None")
print("Registration income: Rs.", registration_income)
print("Sponsorship total   : Rs.", sponsorship_total)
print("Total income        : Rs.", total_income)
print("Total expenses      : Rs.", expense_total)
print("Final balance       : Rs.", balance)
if balance >= 0:
    print("Result: Surplus")
else:
    print("Result: Financial shortfall")
