def yearPayment(balance, annualInterestRate):
    month = 0
    lowestPayment = 10
    monthBalance = balance
    monthlyInterestRate = annualInterestRate / 12
    while  monthBalance >= 0:
		lowestPayment += 10
		monthBalance = balance
		for month in range(1,13):
			monthBalance = (monthBalance - lowestPayment) * (1 + monthlyInterestRate)
		if monthBalance <= 0:
			break
    return lowestPayment	
print 'Lowest Payment: ', yearPayment(balance, annualInterestRate)
