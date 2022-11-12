sum = 0
count = 0
min = None
max = None
mlst = []
while True:
    num = input('Enter a number : ')
    if num == 'done':
        if sum == 0 & count == 0:
            print('insert atleast one number')
            continue
        break
    else:
        try:
            fnum = float(num)
            count += 1
            sum += fnum
            if max is None or fnum>max:
                max = fnum
            if min is None or fnum<min:
                min = fnum
            mlst.append(fnum)
            continue
        except:
            print('Invalid input')
            continue
print('Sum : ', sum, 'Maximum : ', max, 'Minimum : ', min)
print('Number inserted : ', mlst)

# sum = 0
# count = 0
# max = None
# min = None
# mylist = []
# while True:
#     try:
#         num = input('Enter a number : ')
#         if num == 'done':
#             if sum == 0 & count == 0:
#                 print('insert number first')
#                 continue
#             else:
#                 break
#         else:
#             fnum = float(num)
#             if max is None or fnum > max:
#                 max = fnum
#             if min is None or fnum < min:
#                 min = fnum
#             count += 1
#             sum += fnum
#             mylist.append(fnum)
#
#     except:
#         print('Invalid Input')
#         continue
#
# print('Tot : ', sum, 'Maximum : ', max, 'Mininum : ', min)
# print(mylist)
