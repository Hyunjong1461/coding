alist=[]
N,K=map(int,input().split())
for i in range(N):
    k=int(input())
    alist.append(k)
i=0
cnt=0

if alist[-1] <= K:
    K-= alist[-1]
    cnt+=1
else:
    while 1:
        i += 1
        if K==0:
            break

        elif alist[i]>K:
            K-=alist[i-1]
            i=0
            cnt+=1
print(cnt)