n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr)

alist=[]

visited=[0]*(n)

all = []
def dfs(a):

    if a==m:
        print(*alist)

    a=0
    for i in range(n):
        if visited[i]==0 and a != arr[i]:
            alist.append(arr[i])
            visited[i] = 1
            a=arr[i]
            dfs(a + 1)
            alist.pop()
            visited[i] = 0

dfs(0)