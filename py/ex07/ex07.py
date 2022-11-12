while True:
    fname = input('Enter File Name : ')
    try:
        fhand = open(fname)
        count = 0
        for line in fhand:
            count = count + 1
        break
    except:
        print('Wrong File Name, pleas write again')
        continue

print('Lines : ', count)
