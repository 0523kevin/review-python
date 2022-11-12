ffile = input('Enter a file name : ')
fhand = open(ffile)

lst = []

for line in fhand:
    for word in line.rstrip().split():
        if word not in lst:
            lst.append(word)
print(sorted(lst))
