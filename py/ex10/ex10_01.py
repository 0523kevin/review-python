ffile = input('Enter a file : ')
fpage = open(ffile)

lst = []
dic = dict()
for line in fpage:
    words = line.rstrip().split()
    if len(words)<1 or words[0] != 'From':
        continue
    else:
        lst.append(words[1])

for word in lst:
    dic[word] = dic.get(word, 0) + 1

#방법 1
max = None
for k,v in dic.items():
    if max is None or max<v:
        max = v
        key = k
print(key, max)


#방법 2
# list_tup = []
# for k,v in dic.items():
#     tup = (v,k)
#     list_tup.append(tup)
#
# ex = max(list_tup)
# print(ex[1], ex[0])


# ls = dict()
# l = []
# for word in lst:
#     uname, domain = word.split('@')
#     l.append(uname)
# for u in l:
#     ls[u] = ls.get(u,0) + 1
# print(ls)
