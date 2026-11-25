# Case Study 2: Employee Payroll
basic_pay = 25000.0
overtime_hours = 6
incentive = 2000.0

hra = basic_pay * 0.20
travel_allowance = basic_pay * 0.10
overtime_pay = overtime_hours * 150
gross_salary = basic_pay + hra + travel_allowance + overtime_pay + incentive

if gross_salary <= 20000:
    deduction = 0
elif gross_salary <= 30000:
    deduction = (gross_salary - 20000) * 0.05
else:
    deduction = 10000 * 0.05 + (gross_salary - 30000) * 0.10

net_salary = gross_salary - deduction

print("EMPLOYEE SALARY STATEMENT")
print("Basic Pay       : Rs.", round(basic_pay, 2))
print("HRA             : Rs.", round(hra, 2))
print("Travel Allowance: Rs.", round(travel_allowance, 2))
print("Overtime Pay    : Rs.", round(overtime_pay, 2))
print("Incentive       : Rs.", round(incentive, 2))
print("Gross Salary    : Rs.", round(gross_salary, 2))
print("Deduction       : Rs.", round(deduction, 2))
print("Net Salary      : Rs.", round(net_salary, 2))
