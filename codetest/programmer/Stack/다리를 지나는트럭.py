from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck = deque(truck_weights)
    answer = 0
    sum_t = 0
    while bridge:
        answer += 1
        n = bridge.popleft()
        sum_t -= n
        if truck:
            if sum_t + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                sum_t += t
            else:
                bridge.append(0)
    return answer 
        