# 직사각형의 바깥 테두리를 따는 것을 진행해야됨
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    field = [[-1] * 102 for i in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i and i < x2 and y1 < j and j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
    itemX *= 2
    itemY *= 2
    queue = deque()
    queue.append([characterX * 2, characterY * 2])
    while queue:
        x, y = queue.popleft()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        if x == itemX and y == itemY:
            return field[x][y]//2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if field[nx][ny] == 1:
                field[nx][ny] = field[x][y] + 1
                queue.append([nx, ny])
            

# cnt를 매개변수로 갖으며 이동 횟수 쌓기
# from collections import deque
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     answer = 0
#     field = [[-1] * 102 for i in range(102)]
#     for rec in rectangle:
#         x1, y1, x2, y2 = map(lambda x: x*2, rec)
#         for i in range(x1, x2+1):
#             for j in range(y1, y2 + 1):
#                 if x1 < i and i < x2 and y1 < j and j < y2:
#                     field[i][j] = 0
#                 elif field[i][j] != 0:
#                     field[i][j] = 1

#     itemX *= 2
#     itemY *= 2
#     queue = deque()
#     queue.append([characterX * 2, characterY * 2, 0])
#     while queue:
#         x, y, cnt = queue.popleft()
#         dx = [-1,1,0,0]
#         dy = [0,0,1,-1]
#         if x == itemX and y == itemY:
#             answer = cnt // 2
#             break
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= 102 or ny >= 102:
#                 continue
#             if field[nx][ny] < 1:
#                 continue
#             if field[nx][ny] == 1:
#                 field[nx][ny] = field[x][y] + 1
#                 queue.append([nx, ny, cnt + 1])
#     return answer
