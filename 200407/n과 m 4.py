n,m=map(int,input().split())

arr=[]
visited=[0]*(n+1)
def dfs(a):
    global visited
    if a==m:
        if sorted(arr)==arr:
            print(*arr)
            return
    else:
        for i in range(1,n+1):
                arr.append(i)
                dfs(a+1)
                arr.pop()

dfs(0)