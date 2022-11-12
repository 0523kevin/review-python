# 반복 출력
def computepay(hh, rr):
    if hh>40:
        pay = (hh-40)*rr*1.5 + 40*rr
    else:
        pay = hh*rr
    print('Pay : ', pay)

while True:
    try:
        hh = input('Enter a Hour : ')
        fh = float(hh)
        rr = input('Enter a Rate : ')
        fr = float(rr)
        computepay(fh, fr)
        break
    except:
        print('insert a numeric input')
        continue


# 단순 출력
# def computepay(hh, rr):
#     try:
#         fh = float(hh)
#         fr = float(rr)
#     except:
#         print('insert numeric input')
#         quit()
#     if fh>40:
#         pay = (fh-40)*fr*1.5 + 40*fr
#     else:
#         pay = fh*fr
#     print(pay)
#
# hh = input('Enter Hours : ')
# rr = input('Enter Rate : ')
#
# computepay(hh,rr)


# def computepay(hours, rate):
#
#     try:
#         fh = float(hours)
#         fr = float(rate)
#         pp = fh*fr
#
#         if fh<=40:
#             print('Pay: ', pp)
#         else:
#             pp = (fh-40)*fr*1.5 + 40*fr
#             print('Pay: ', pp)
#
#     except:
#         print('Not a number')
#
# hh = input('Enter Hours : ')
# rr = input('Enter Rate : ')
#
# computepay(hh, rr)
