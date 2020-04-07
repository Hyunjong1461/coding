from _collections import deque

n,m,v=map(int,input().split())
arr=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a]=sorted(arr[a])
    arr[b]=sorted(arr[b])
print(arr)

def dfs(v):
    stack=[]
    visit=[]
    stack.append(v)
    while stack:
        q=stack.pop()
        if q not in visit:
            visit.append(q)
            stack.extend(reversed(arr[q]))
    print(*visit)
dfs(v)

def bfs(v):
    Q=deque()
    visit = []
    Q.append(v)
    while Q:
        q=Q.popleft()
        if q not in visit:
            visit.append(q)
            Q.extend(arr[q])
    print(*visit)
bfs(v)



#
#
#
# def dfs(v):
#     stack=[]
#     visit = []
#     visited = [0] * (n + 1)
#     stack.append(v)
#     visited[v]=1
#     while stack:#
#         q=stack.pop()
#         visit.append(q)
#         for i in range(m):
#             stack1=[]
#             if arr[i][0] == q:
#                 if visited[arr[i][1]] == 0:
#                     stack1.append(arr[i][1])
#                     visited[arr[i][1]] = 1
#             elif arr[i][1] == q:
#                 if visited[arr[i][0]] == 0:
#                     Q.append(arr[i][0])
#                     visited[arr[i][0]] = 1
#
#     print(*visit)
# dfs(v)
# def bfs(v):
#     Q = deque()
#
#     visit = []
#     visited = [0] * (n + 1)
#     Q.append(v)
#     visited[v] = 1
#     while Q:
#         q=Q.popleft()
#         visit.append(q)
#         for i in range(m):
#             if arr[i][0]==q:
#                 if visited[arr[i][1]]==0:
#                     Q.append(arr[i][1])
#                     visited[arr[i][1]]=1
#             elif arr[i][1]==q:
#                 if visited[arr[i][0]]==0:
#                     Q.append(arr[i][0])
#                     visited[arr[i][0]]=1
#     print(*visit)
#
# bfs(v)
