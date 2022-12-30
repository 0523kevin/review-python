from collections import Counter
def solution(participant, completion):
    answer = ''    
    par = Counter(participant)
    while completion:
        n = completion.pop()
        par[n] -= 1
    for k, v in par.items():
        if v > 0:
            answer = k
    return answer


#other person's
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]