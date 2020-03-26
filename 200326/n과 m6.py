n,m=map(int,input().split())

arr=sorted(list(map(int,input().split())))
visited=[0]*n
ans=[]
def dfs(a):
    global arr
    if a==m:
        if ans==sorted(ans):
            print(*ans)
    else:
        for i in range(n):
            if visited[i]==1:continue
            visited[i]=1
            ans.append(arr[i])
            dfs(a+1)
            visited[i]=0
            ans.pop()
dfs(0)