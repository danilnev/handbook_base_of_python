summ = 0
while (price := float(input())) != 0:
    if price < 500:
        summ += price
    else:
        summ += price * 0.9
print(summ)
