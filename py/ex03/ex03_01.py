hh = input('Enter Hours : ')
rr = input('Enter Rate : ')

fh = float(hh)
fr = float(rr)

if fh>40:
    pay = fr*40 + fr*1.5(fh-40)
else:
    pay = fr*fh

print('Pay :', pay)







# hh = input('Enter Hours : ')
# rr = input('Enter Rate : ')
#
# try:
#     fh = float(hh)
#     fr = float(rr)
#     pp = fh*fr
#
#     if fh<=40:
#         print('Pay: ', pp)
#     else:
#         pp = (fh-40)*fr*1.5 + 40*fr
#         print('Pay: ', pp)
#
# except:
#     print('Not a number')
