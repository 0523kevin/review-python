ffile = input('Enter a file name : ')
fhand = open(ffile)

dic = {}
lst = []
for line in fhand:
    words = line.rstrip().split()
    if len(words)<1 or words[0] != 'From':
        continue
    else:
        lst.append(words[2])
for text in lst:
    dic[text] = dic.get(text, 0) + 1


sc = {k:v for k,v in sorted(dic.items(), key = lambda item:item[0], reverse = True)}
print(sc)
