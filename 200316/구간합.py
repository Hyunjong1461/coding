u=int(input())

for tc in range(1,u+1):
    maxvalue=0
    minvalue=10000000
    m,n=map(int,input().split())
    alist=list(map(int,input().split()))

    for i in range(m-n+1):
        value=0
        for j in range(n):
            value+=alist[i+j]
        if value>maxvalue:
            maxvalue=value
        if value<minvalue:
            minvalue = value
    print('#{} {}'.format(tc,maxvalue-minvalue))