# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 1
extra_payment_start_month = input('Enter the payment start month:')
extra_payment_end_month = input('Enter the payment end month:')
extra_payment = input('Enter the payment amount:')

while principal > 0:
    if current_month >= int(extra_payment_start_month) and current_month <= int(extra_payment_end_month):
        principal = principal * (1+rate/12) - (payment + float(extra_payment))
        total_paid = total_paid + (payment + float(extra_payment))
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    if principal > 0:
        print(f'{current_month:4d} {total_paid:8.2f} {principal:8.2f}')
        current_month = current_month + 1

print('Total paid', round(total_paid, 2))
print('Months', current_month)