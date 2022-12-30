#정답
def solution(s):
    answer = True
    done = []
    cnt1 = s.count('(')
    cnt2 = s.count(')')
    if len(s) % 2 != 0:
        answer = False
    else:
        if s.startswith('(') and s.endswith(')'):
            if cnt1 != cnt2:
                answer = False
            else:
                for i in s:
                    if i == '(':
                        done.append(i)
                    else:
                        if done == []:
                            answer = False
                        else:
                            done.pop()
                        
        else:
            answer = False

    return answer

