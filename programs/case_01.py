# Case Study 1: Progressive Electricity Billing
# Sample tariff for academic demonstration only.
monthly_units = [80, 110, 160]
fixed_charge = 40.0

def energy_charge(units):
    charge = 0.0
    first = min(units, 100)
    second = min(max(units - 100, 0), 100)
    third = max(units - 200, 0)
    charge += first * 2.00
    charge += second * 3.00
    charge += third * 5.00
    return charge

bills = []
for month_number, units in enumerate(monthly_units, start=1):
    bill = energy_charge(units) + fixed_charge
    if units <= 100:
        bill = bill - (bill * 0.05)
    bills.append(bill)
    print("Month", month_number, "| Units:", units, "| Bill: Rs.", round(bill, 2))

print("\nUnusual increases:")
found = False
for i in range(1, len(bills)):
    if bills[i] > bills[i - 1] * 1.25:
        print("Month", i + 1, "bill increased by more than 25%.")
        found = True
if not found:
    print("No unusual increase detected.")
