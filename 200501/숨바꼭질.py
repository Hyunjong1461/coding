from collections import deque
n, k = map(int, input().split())
visit = [0]*100001

q = deque()
q.append([n, 0])
while q:
    p, cnt = q[0][0], q[0][1]
    if p == k:
        break
    q.popleft()
    visit[p] = 1
    if p - 1 >= 0 and visit[p - 1] == 0:
        q.append([p - 1, cnt + 1])
    if p + 1 <= 100000 and visit[p + 1] == 0:
        q.append([p + 1, cnt + 1])
    if p * 2 <= 100000 and visit[p * 2] == 0:
        q.append([p * 2, cnt + 1])
print(q[0][1])