# # ~ 시작하는 줄에서 숫자 추출 후 평균 구하기
# fname = input('Enter a file name : ')
#
# tot = 0
# count = 0
# try:
#     text = open(fname)
# except:
#     print('Input file nofound')
#     quit()
#
# for line in text:
#     rline = line.rstrip()
#     words = rline.split()
#     if rline.startswith('X-DSPAM-Confidence:'):
#         print(rline)
#         dig = rline.find(':')
#         #print(rline)
#         num = float(rline[dig+1:])
#         tot += num
#         count += 1
#
# print('Average spam confidence: ', tot/count)


fname = input('Enter a file name : ')

tot = 0
count = 0
try:
    fpage = open(fname)
except:
    print('file not found')
    quit()
for line in fpage:
    rline = line.rstrip()
    words = rline.split()
    if rline.starswith('X-DSPAM-Confidence : '):
        print(rline)
        dig = rline.find(':')
        num = float(rline[dig+1:])
