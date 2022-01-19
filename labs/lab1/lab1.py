"""
Carson Shields
lab1.py
write a function to compute the monthly interest amount on a credit card bill.

I certify that all work shown below is my own: CS

"""


def monthly_interest():
    annual_IR = eval(input("enter Annual interest rate: "))
    num_days_bill_cycle = eval(input("enter the number of days in the billing period: "))
    previous_net_bal = eval(input("enter the previous net balance on account: "))
    payment_amount = eval(input("enter the amount of the payment: "))
    day_of_cycle_payment_made = eval(input("enter which day of the billing cycle the payment was made: "))

    step1 = previous_net_bal * num_days_bill_cycle
    step2 = payment_amount * (num_days_bill_cycle - day_of_cycle_payment_made)
    step3 = step1 - step2
    avg_daily_bal = step3 / num_days_bill_cycle


    monthly_IR = (annual_IR / 12) / 100
    amount = round(avg_daily_bal * monthly_IR, 2)



    print("the average monthly interest payment is: ", amount)

