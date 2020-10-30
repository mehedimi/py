
hourly_wage = float(input('Enter wage amount: '))
regular_hour = float(input('Enter regular working hour: '))
overtime_hour = float(input('Enter overtime working hour: '))

hourly_pay = hourly_wage * regular_hour
overtime_pay = 1.5 * hourly_wage * overtime_hour
pay = hourly_pay + overtime_pay

print("Total weekly pay: " + str(pay))
