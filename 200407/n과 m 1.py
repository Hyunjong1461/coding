n,m=map(int,input().split())

arr=[]
visited=[0]*(n+1)
def dfs(a):
    global visited
    if a==m:

        print(*arr)
        return
    else:
        for i in range(1,n+1):
            if visited[i]==0:
                visited[i]=1
                arr.append(i)
                dfs(a+1)
                arr.pop()

                visited[i]=0
dfs(0)