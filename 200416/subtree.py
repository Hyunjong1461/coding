t=int(input())
for tc in range(1,t+1):
    alist=[]
    E,N=map(int,input().split())
    arr=list(map(int,input().split()))
    for i in range(0,2*E,2):
        (a,b)=(arr[i],arr[i+1])
        alist.append((a,b))
    # print(E,N,alist)
    stack=[]
    stack.append(N)
    visit=[]
    while stack:
        a = stack.pop()
        visit.append(a)
        for i in range(E):
            if alist[i][0]==a:
                stack.append(alist[i][1])
    print('#{} {}'.format(tc,len(visit)))