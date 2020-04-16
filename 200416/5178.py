for tc in range(1,int(input())+1):
    N,M,L=map(int,input().split())
    T=[0]*(N+1)
    for _ in range(M):
        idx,val =map(int,input().split())
        T[idx]=val


    # for i in range(N,1,-1):
    #     T[i//2]+=T[i]

    def postorder(idx):
        if idx>N:return 0
        T[idx]+=postorder(idx*2)
        T[idx]+=postorder(idx*2+1)
        return T[idx]
    postorder(1)
    print(T[L])