n ,m = map(int,input().split())
visited=[0]*n
arr=[]
def dfs(a):
    global arr
    if a==m:
        print(*arr)
    else:
        for i in range(0,n):
            if visited[i]==1:continue
            visited[i]=1
            arr.append(i+1)
            dfs(a+1)
            visited[i]=0
            arr.pop()

dfs(0)