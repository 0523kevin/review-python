ffile = input('Enter a file name : ')
fname = open(ffile)

dic = {}
lst = []

for line in fname:
    words = line.rstrip().split()
    if len(words) < 1 or words[0] != 'From':
        continue
    else:
        lst.append(words[1])

for word in lst:
    dic[word] = dic.get(word,0) + 1


max=None

# mylst = sorted(dic)
for k,v in dic.items():
    if max is None or max<v:
        max = v
        key = k

print(key, max)

# for k,v in dic.items():
#     if max is None or max>int(v):
#         max = int(v)
# print(dic.keys(max), max)
# sc = {k:v for k,v in sorted(dic.items(), key = lambda item:item[1], reverse = True)}
# sc[]
