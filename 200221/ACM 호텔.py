T=int(input())

for _ in range(T):
    H,W,N = map(int,input().split())


    cnt =0
    for i in range(1,W+1):
        for j in range(1,H+1):
            cnt+=1
            if cnt==N:
                j1=str(j)
                i1=str(i)
                if len(i1)==1:
                    print(j1+'0'+i1)
                else:
                    print(j1+i1)