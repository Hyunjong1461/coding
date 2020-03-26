n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
visited=[0]*n
ans=[]
def dfs(a):
    global arr,ans
    if a==m:
        print(*ans)
        return

    else:
        check=0
        for i in range(n):
            if visited[i]==1 or check==arr[i]:continue
            visited[i]=1
            ans.append(arr[i])
            check=arr[i]
            dfs(a+1)
            visited[i]=0
            ans.pop()
dfs(0)