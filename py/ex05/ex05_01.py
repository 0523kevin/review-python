sum = 0
count = 0
while True:
    num = input('Enter a number : ')
    if num == 'done':
        if sum == 0 or count == 0:
            print("You should insert atleast one number to press 'done'")
            continue
        else:
            break
    else:
        try:
            fnum = float(num)
            sum += fnum
            count += 1
            continue
        except:
            print('Invalid input. Please insert numeric input')
            continue

print('Sum of all input number : ', sum)
print('Average : ', sum/count)
# sum = 0
# count = 0
# while True:
#     try:
#         num = input('Enter a number : ')
#         if num == 'done':
#             if sum == 0 & count ==0: #숫자 입력 없이 바로 done 을 입력 했을 때 다시 입력 할 수 있도록 유도
#                 print('you have to insert number before inserting done')
#                 continue
#             else:
#                 break
#         else:
#             fnum = float(num)
#             count += 1
#             sum += fnum
#
#     except:
#         print('Invalid Input')
#         continue
#
# print(sum, sum/count)
