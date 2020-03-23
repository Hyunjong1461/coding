i= int(input())

for tc in range(1,i+1):
    a=int(input())
    alist=list(map(int,input().split()))
    n=len(alist)
    for j in range(n-1,0,-1):
        for i in range(j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
    print('#{} {}'.format(tc,alist[-1]-alist[0]))