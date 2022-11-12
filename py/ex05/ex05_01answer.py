count = 0
tot = 0.0
while True :
    sval = input('Enter a number : ')

    if sval == 'done':
        break
    try:
        fval = float(sval)
        count = count + 1
        tot = tot + fval
    except:
        print('Invalid Input')
        continue
print(tot, count, tot/count)
