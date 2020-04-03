from _collections import deque


t=int(input())
for tc in range(1,t+1):
    Q = deque()
    Q1=deque()
    arr = deque()
    m,n=map(int,input().split())
    Q=deque(map(int,input().split()))

    for i in range(len(Q)):
        Q1.append((Q[i],i))

    while len(Q1)>0:
        if max(Q)==Q1[0][0]:
            arr.append(Q1.popleft())
            Q.popleft()
        else:
            Q1.append(Q1.popleft())
            Q.append(Q.popleft())
    cnt=0
    for i in range(len(arr)):
        if arr[i][1]!=n:
            cnt+=1
        else:
            cnt+=1
            print(cnt)
            break
