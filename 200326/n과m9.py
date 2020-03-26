n,m=map(int,input().split())
arr=sorted(list(map(int,input().split())))
visited=[0]*n
ans=[]
ansans = []

def dfs(a):
    global arr,ans,ansans
    if a==m:
        if ans not in ansans:
            ansans+=ans[:]
            print(ans[:])
    else:
        for i in range(n):
            if visited[i]==1:continue
            visited[i]=1
            ans.append(arr[i])
            dfs(a+1)
            visited[i]=0
            ans.pop()
dfs(0)