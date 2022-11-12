fname = input('Enter a File name: ')
if len(fname)<1:fname = 'clown.txt'

hand = open(fname)

di = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

print(di)

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse = True)
for v,k in tmp[:5]:
    print(k,v)

# print('Sorted', tmp[:5])
