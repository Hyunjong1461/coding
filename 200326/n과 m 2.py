n ,m = map(int,input().split())
visited=[0]*(n+1)
arr=[]
def dfs(a):
    global arr
    if a==m:
        if arr==sorted(arr):
            print(*arr)
    else:
        for i in range(0,n):
            if visited[i]==1:continue
            visited[i]=1
            arr.append(i+1)
            dfs(a+1)
            arr.pop()
            visited[i]=0

dfs(0)