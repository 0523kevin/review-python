while True:
    try:
        sr = float(input('Enter score : '))

        if sr>=1.0:
            print('Bad score')
            continue
        if sr>=0.9:
            print('A')
        elif sr>=0.8:
            print('B')
        elif sr>=0.7:
            print('C')
        elif sr>=0.6:
            print('D')
        else:
            print('F')
    except:
        print('Bad score')
        continue
