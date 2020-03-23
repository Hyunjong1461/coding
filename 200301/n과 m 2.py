m,n=map(int,input().split())
visit=[0]*(m+1)
arr=[]
def dfs(a):
    if a==n:
        print(*arr)

        print(*visit)
    else:
        for i in range(1,m+1):
            if visit[i]:continue
            visit[i]=1
            arr.append(i)
            dfs(a+1)
            arr.pop()
            for j in range(i+1,m+1):
                visit[j]=0
dfs(0)