from collections import deque
n,k=map(int,input().split())
arr=deque()
arr.append([n,0])
visit=[0]*100001


while arr:
    q, cnt = arr[0][0], arr[0][1]
    if q==k:
        break
    visit[q] = 1
    arr.popleft()
    if 2 * q <=100000 and visit[q * 2] == 0:
        arr.append([q * 2,cnt+1])

    if q+1 <=100000 and visit[q + 1]==0:
        arr.append([q + 1, cnt + 1])

    if q-1 >=0 and visit[q - 1]==0:
        arr.append([q - 1, cnt + 1])
print(arr[0][1])
