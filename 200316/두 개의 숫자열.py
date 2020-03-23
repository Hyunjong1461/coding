t = int(input())

for tc in range(1,t+1):
    m,n=map(int,input().split())
    mlist=list(map(int,input().split()))
    nlist=list(map(int,input().split()))
    maxvalue=0

    if m<n:
        for i in range(n-m+1):
            value=0
            for j in range(m):
                value+=nlist[i+j]*mlist[j]
            if value>maxvalue:
                maxvalue=value
    else:
        for i in range(m-n+1):
            value=0
            for j in range(n):
                value+=nlist[j]*mlist[i+j]
            if value>maxvalue:
                maxvalue=value
    print('#{} {}'.format(tc,maxvalue))