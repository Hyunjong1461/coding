arr='ABC'; N=len(arr)

perm=[]
visit=[0]*N
for i in range(N):
    if visit[i]:continue
    perm.append(arr[i]);visit[i]=1
    
    for j in range(N):
        # if arr[j] in perm : continue
        if visit[j]:continue
        perm.append(arr[j]);visit[j]=1

        # if j==i:continue
        for k in range(N):
            # if k==i or k==j: continue
            # if arr[k] in perm: continue
            if visit[k]: continue
            perm.append(arr[k]);visit[k]=1

            print(perm)
            perm.pop();visit[k]=0
        perm.pop();visit[j]=0
    perm.pop();visit[i]=0