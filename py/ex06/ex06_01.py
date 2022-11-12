str = 'X-DSPAM - Confidence : 0.8475'
col = str.find(':')
por = str[col+1:]
fpor = float(por)

print(round(fpor, 2))
