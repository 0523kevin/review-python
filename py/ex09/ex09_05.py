ffile = input('Enter a file : ')
fpage = open(ffile)

lst = []
for line in fpage:
    words = line.rstrip().split()
    if line.startswith('From '):
        lst.append(words[2])



# ffile = input('Enter a file name : ')
# fname = open(ffile)
#
# dic = {}
# lst = []
#
# for line in fname:
#     words = line.rstrip().split()
#     if len(words) < 1 or words[0] != 'From':
#         continue
#     else:
#         lst.append(words[1])
#
# list = []
# for e in lst:
#     slst = e.split('@')
#     list.append(slst[1])
# for w in list:
#     dic[w] = dic.get(w, 0) + 1
# print(list)
# print(dic)

##
# ffile = input('Enter a file : ')
# fpage = open(ffile)
#
# lst = []
# for line in fpage:
#     words = line.rstrip().split()
#     if line.startswith('From '):
#         lst.append(words[2])
# print(lst)
# print(len(lst))
# print(lst.count('Fri')/len(lst))
