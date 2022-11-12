while True:

    try:
        hour = float(input('Enter Hours : '))
        rate = float(input('Enter Rate : '))
        pay = round(hour * rate,2)
        break
    except:
        print('Insert number only')
        continue
print('Pay : ', pay)
