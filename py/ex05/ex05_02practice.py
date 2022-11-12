tot = 0.0
count = 0
list = []
largest = None
smallest = None

while True:
    sval = input('Enter a number : ')

    if sval == 'done':
        break
    try:
        fval = float(sval)
        tot = tot + fval
        count = count + 1
        list.append(fval)
        for num in list:
            if largest is None or num>largest:
                largest = num
            if smallest is None or num<smallest:
                smallest = num
    except:
        print('Invalid input')
        continue

print('Total : ', tot, 'How many number used : ', count, 'Average : ', tot/count)
print('Maximum : ', largest)
print('Minimum : ', smallest)
