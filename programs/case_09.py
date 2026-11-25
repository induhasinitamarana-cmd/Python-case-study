# Case Study 9: Tuple-Based Product Catalogue Audit
products = [
    ("P101", "Keyboard", 750.0, 8),
    ("P102", "Mouse", 350.0, 3),
    ("P103", "Monitor", 6500.0, 2),
    ("P104", "USB Cable", 150.0, 12)
]
inventory_value = 0.0
replenishment = []

print("PRODUCT CATALOGUE AUDIT")
for product_id, name, price, quantity in products:
    if price < 0 or quantity < 0:
        print("Invalid record:", product_id)
    else:
        value = price * quantity
        inventory_value += value
        print(product_id, name, "| Price:", price,
              "| Quantity:", quantity, "| Value:", value)
        if quantity < 5:
            replenishment.append(name)

print("Total inventory value: Rs.", round(inventory_value, 2))
print("Products requiring replenishment:",
      replenishment if replenishment else "None")
