from _collections import deque
n=int(input())

t=int(input())
arr=[]
for i in range(t):
    a,b=map(int,input().split())
    arr.append((a,b))

Q=deque()


visit=[]
visited=[0]*(n+1)

Q.append(1)
visited[1]=1


while Q:
    q=Q.popleft()
    visit.append(q)

    for i in range(t):
        if arr[i][0] == q:
            if visited[arr[i][1]]==0:
                Q.append(arr[i][1])
                visited[arr[i][1]]=1
        elif arr[i][1]==q:
            if visited[arr[i][0]] == 0:
                Q.append(arr[i][0])
                visited[arr[i][0]] = 1
cnt=0
for i in range(len(visited)):
    if visited[i]==1:
        cnt+=1
print(cnt-1)

