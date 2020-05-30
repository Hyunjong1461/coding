t=int(input())

for tc in range(1,t+1):
    N=int(input())
    L=[0]*(N+1)
    cnt=1
    def tree(x):
        if x>N:return
        tree(2*x)
        global cnt
        L[x]=cnt
        cnt+=1
        tree(2*x+1)

    tree(1)
    print('#{} '.format(tc),end='')
    print(L[1],L[N//2])