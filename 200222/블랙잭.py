n,m=map(int,input().split())
arr=list(map(int,input().split()))
ans=[]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if i!=j:
            for k in range(j, len(arr)):
                if i!=k and j!=k:
                    a=(arr[i]+arr[j]+arr[k])
                    if a<=m:
                        ans.append(a)
print(max(ans))

