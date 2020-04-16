from _collections import deque

t=int(input())
arr=[]
flag=True
while flag==True:
    m,n=map(int,input().split())
    if m==-1 and n==-1:
        flag=False
    else:
        arr.append((m, n))


ans=[]
for i in range(1,t+1):
    Q = deque()
    visit = []
    visited = [0] * (t + 1)
    Q.append(i)
    visited[i]=1
    while Q:
        q=Q.popleft()
        visit.append(q)

        for j in range(len(arr)):
            if arr[j][0]==q:
                if visited[arr[j][1]]==0:
                    Q.append(arr[j][1])
                    visited[arr[j][1]]=visited[q]+1
            elif arr[j][1] == q:
                if visited[arr[j][0]]==0:
                    Q.append(arr[j][0])
                    visited[arr[j][0]]=visited[q]+1
    ans.append(max(visited)-1)

cnt=0
for i in range(len(ans)):
    if ans[i]==min(ans):
        cnt+=1

print('{} {}'.format(min(ans),cnt))
for i in range(len(ans)):
    if ans[i] == min(ans):
        print(i+1,end=' ')

