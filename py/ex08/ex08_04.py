# 첫번째 해결~
fname = input('Enter a file name : ')

try:
    ffile = open(fname)
except:
    print('insert valid file name')
    quit()

dict = {}
mylst = []

for text in ffile:
    rtext = text.rstrip()
    words = rtext.split()
    for word in words:
        dict[word] = dict.get(word, 0) + 1
    for k,v in dict.items():
        if v<=1:
            mylst.append(k)
print(sorted(mylst))


#2번째 해결책
fname = input('Enter a file name : ')

try:
    ffile = open(fname)
except:
    print('insert valid file name')
    quit()

lst = []
for line in ffile:
    for word in line.rstrip().split():
        if word not in lst:
            lst.append(word)
print(sorted(lst))
