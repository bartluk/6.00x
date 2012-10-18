monthlyInterestRate = annualInterestRate / 12

tp = 0
for month in range(1,13,1):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    balance = (balance - minimumMonthlyPayment) * (1 + monthlyInterestRate)
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment, 2))
    print 'Remaining balance: ' + str(round(balance, 2))
    month =+ 1
    tp += minimumMonthlyPayment
print 'Total paid: ', round(tp, 2)
print 'Remaining balance: ', round(balance, 2)
