fname = input('Enter a file name : ')

try:
    ffile = open(fname)
except:
    print('insert valid file name')
    quit()

for text in ffile:
    rtext = text.rstrip()
    words = rtext.split()

    if len(words)<1 or words[0] != 'From':
        continue
    print(words[2])
