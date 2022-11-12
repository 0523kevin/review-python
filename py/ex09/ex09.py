ffile = input('Enter a file to predict most frequent word : ')
text = open(ffile)

mydict = dict()

for line in text:
    words = line.split()
    for word in words:
        mydict[word] = mydict.get(word, 0) + 1

bigcount = None
bigword = None

for word, count in mydict.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

print(bigword, bigcount)
