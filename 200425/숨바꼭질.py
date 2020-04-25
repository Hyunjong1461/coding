def dfs(n):
    global cnt
    if n==k:
        return cnt
    else:
        if (k-2*n)<(k-(n+1)) and (k-2*n)<(k-(n-1)):
            n=n*2
            cnt+=1

        else:
            if (k-(n+1))>(k-(n-1)):
                n=n-1
                cnt+=1

            else:
                n=n+1
                cnt+=1
        dfs(n)
n,k=map(int,input().split())
cnt=0
dfs(n)
print(cnt)

