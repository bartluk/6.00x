def genPrimes():
    primes_list = []
    x = 1
    while True:
        x +=1 
        for n in primes_list:
            if x % n == 0:
                break
        else:
            primes_list.append(x)
            yield x