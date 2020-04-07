n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr=sorted(arr)

alist=[]
k=[-100]
visited=[0]*(n)
def dfs(a):
    global alist, k
    if a==m:
        print(alist)

        return
    else:
        for i in range(n):
            if visited[i]==0:
                alist.append(arr[i])
                if alist == k:
                    alist.pop()
                visited[i]=1
                dfs(a+1)
                k=[*alist]
                alist.pop()
                visited[i] = 0
dfs(0)