ffile = input('Enter a file name : ')
fhand = open(ffile)

dic = {}
lst = []
for line in fhand:
    words = line.rstrip().split()
    if len(words)<1 or words[0] != 'From':
        continue
    else:
        lst.append(words[1])

for word in lst:
    dic[word] = dic.get(word, 0) + 1

sc = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1],reverse = True)}
print(sc)
