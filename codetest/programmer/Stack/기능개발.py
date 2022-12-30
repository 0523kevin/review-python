import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    answer_list = []
    proba = deque()
    done = []
    for k, v in zip(progresses, speeds):
        proba.append(math.ceil((100 - k)/v))
    for i in range(len(proba)):
        n = proba.popleft()
        if done == []:
            done.append(n)
        else:
            if n <= done[0]:
                done.append(n)
            elif n > done[0]:
                answer.append(len(done))
                done.clear()
                done.append(n)
    answer.append(len(done))
    for i in answer_list:
        answer.append(len(i))
                
    return answer