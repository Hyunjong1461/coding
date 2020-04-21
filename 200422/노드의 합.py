t= int(input())
for tc in range(1,t+1):
    n,m,l=map(int,input().split())
    L=[0]*(n+1)
    for i in range(m):
        a,b=map(int,input().split())
        L[a]=b
    print(L)

    def tree(k):
        if k>n:return 0
        L[k]+=tree(2*k)
        L[k]+=tree(2*k+1)
        return L[k]

    tree(1)
    print(L[l])