max = None
min = None


while True:
    try:
        num = input('Enter a number: ')

        if num == 'done':
            break
        else:
            fnum = float(num)

            if max is None or max<fnum:
                max = fnum
            if min is None or min>fnum:
                min = fnum
    except:
        print('Invalid input')
        continue

print('Maximum : ', max)
print('Minimum : ', min)
