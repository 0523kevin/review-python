fname = input('Enter File name : ')
file = open(fname)

lst = []
for line in file:
    rline = line.rstrip()
    words = rline.split()
    if rline.startswith('X-DSPAM-Confidence'):
        lst.append(words)
    # print(words)
print(lst[0])
