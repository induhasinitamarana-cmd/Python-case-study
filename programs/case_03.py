# Case Study 3: Retail Billing
products = [
    ("Notebook", "stationery", 80.0, 10),
    ("Rice Bag", "grocery", 650.0, 2),
    ("Pen Pack", "stationery", 120.0, 3)
]
tax_rates = {"grocery": 0.05, "stationery": 0.12, "other": 0.18}
subtotal = 0.0
tax_total = 0.0

print("ITEMIZED RETAIL INVOICE")
for name, category, price, quantity in products:
    line_total = price * quantity
    tax = line_total * tax_rates.get(category, tax_rates["other"])
    subtotal += line_total
    tax_total += tax
    print(name, "|", quantity, "x Rs.", price,
          "| Amount: Rs.", round(line_total, 2),
          "| Tax: Rs.", round(tax, 2))

discount = 0.0
if subtotal >= 2000:
    discount = min(subtotal * 0.10, 500.0)

final_amount = subtotal - discount + tax_total
print("Subtotal     : Rs.", round(subtotal, 2))
print("Discount     : Rs.", round(discount, 2))
print("Total Tax    : Rs.", round(tax_total, 2))
print("Grand Total  : Rs.", round(final_amount, 2))
