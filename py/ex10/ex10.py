ffile = input('Enter a file : ')
fpage = open(ffile)

lst = list()
di = dict()
for line in fpage:
    words = line.rstrip().split()
    for word in words:
        di[word] = di.get(word, 0) + 1

for k,v in di.items():
    tup = (v,k)
    lst.append(tup)

lst = sorted(lst, reverse=True)
for v,k in lst[:15]:
    print(v,k)

#list comprehension
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [int(x) for x in list_of_ints_in_strings]
print(sum(list_of_ints))


# d = {'a': 10, 'b': 1, 'c': 9}
# t = sorted(d.items())
# print(t)
# for k,v in t:
#     print(k, v)

#sort by values instead of key
c = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))

print(tmp)

tmp = sorted(tmp, reverse = True)
print(tmp)


#top10 most common
# ffile = input('Enter a file name: ')
# text = open(ffile)
# mydi = dict()
# for line in text:
#     line = line.rstrip()
#     words = line.split()
#
#     for word in words:
#         mydi[word] = mydi.get(word, 0) + 1
# print(mydi)

# lst = list()
# for k,v in mydi.items():
#     newtup = (v,k)
#     lst.append(newtup)
# lst = sorted(lst, reverse = True)
#
# for v,k in lst[:10]:
#     print(k)


# print(sorted([(v,k) for k,v in mydi.items()]))
