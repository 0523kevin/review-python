ffile = input('Enter a file name : ')
fhand = open(ffile)

lst = []
count = 0
for line in fhand:
    words = line.rstrip().split()
    # print(words)
    if len(words)<1 or words[0] != 'From':
        continue
    else:
        count += 1
        print(words[1])

print('There were ', count, ' lines in the file with "From" as the first word')
