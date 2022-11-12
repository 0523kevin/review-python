fname = input('Enter a File name: ')
if len(fname)<1:fname = 'clown.txt'

hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()

    words = line.split()
    for word in words:
        if word in di:
            di[word] = di[word] + 1
            print('***Existing***')
        else:
            di[word] = 1
            print('***New***')
        print(word, di[word])
