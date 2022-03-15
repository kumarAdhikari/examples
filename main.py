def how_to_pay(amount, currency):
    currency = sorted(currency)
    dicto = {}
    x = 0
    numbers = len(currency)
    biggestbill = currency[-1]
    #biggestbill)
    #print(currency)
    while amount != 0:
        if amount >= biggestbill:
            x += 1
            dicto[biggestbill] = x
            amount = amount - biggestbill
            if amount != biggestbill and amount < biggestbill:
                x = 0
                numbers = numbers -1
                biggestbill = currency[numbers]
        else:
            numbers = numbers - 1
            biggestbill = currency[numbers]
            continue

    return dicto

#print(how_to_pay(100, [50, 20, 10, 5]))

#how_to_pay(1, [1, 2, 5, 10, 20, 50, 100, 200, 500])