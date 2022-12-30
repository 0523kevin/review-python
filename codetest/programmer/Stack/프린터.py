# 나의 답
from collections import deque
def solution(priorities, location):
    answer = 0 
    doc = [False] * len(priorities)
    doc[location] = True
    dq_pri = deque(priorities)
    stack = []
    dic = dict(zip(priorities, doc))
    dq_dic = deque(zip(priorities, doc))
    cnt = 0
    while True:
        a = dq_dic.popleft()
        maxi = max(dq_pri)
        b = dq_pri.popleft()
        print(a[0], maxi)
        if a[0] == maxi:
            stack.append(a)
            print(stack)
            cnt += 1
            if a[1] == True:
                answer = cnt
                break
        elif a[0] != maxi:
            dq_dic.append(a)
            dq_pri.append(b)
            
    return answer


# 다른사람 답
def solution(priorities, location):
    answer = 0
    while True:
        for i in range(len(priorities)):
            maximum = max(priorities)
            if priorities[i] == maximum:
                answer += 1
                priorities[i] = 0
                print(priorities)
                maximum = max(priorities)
                if location == i: 
                    return answer