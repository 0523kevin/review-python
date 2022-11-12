def computegrade(grade):
    if grade>=1.0:
        print('Bad score')
    if grade>=0.9:
        print('A')
    elif grade>=0.8:
        print('B')
    elif grade>=0.7:
        print('C')
    elif grade>=0.6:
        print('D')
    else:
        print('F')


while True:
    try:
        grade = input('Enter score : ')
        gr = float(grade)
        computegrade(gr)
        continue
    except:
        print('Bad score')
        continue
