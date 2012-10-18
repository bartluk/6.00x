monthlyInterestRate = annualInterestRate/12

def monthlyPayment(balance, payment):
    for month in range(1,13,1):
        balance = (balance - payment) * (1 + monthlyInterestRate)
    return balance

monthBalance = balance
lower = balance/12
upper = (balance*(1 + monthlyInterestRate)**12)/12
payment = 0.0
while monthBalance < -0.01 or monthBalance > 0.01:
    monthBalance = monthlyPayment(balance, payment)
    if monthBalance < -0.01:
        upper = payment
    elif monthBalance > 0.01:
        lower = payment
    payment = (lower + upper) / 2
print "Lowest Payment: ", round(payment, 2)
