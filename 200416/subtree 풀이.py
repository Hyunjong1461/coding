for tc in range(1,int(input())+1):
    E,N = map(int,input().split())
    arr = list(map(int,input().split()))
    L=[0]*(E+2)
    R=[0]*(E+2)
    for i in range(0,len(arr),2):
        p,c=arr[i],arr[i+1]
        if L[p]:R[p]=c
        else: L[p]=c

    cnt=0
    def subTree(v):
        global cnt
        if v==0: return
        cnt +=1
        subTree(L[v])
        subTree(R[v])

    subTree(N)
    print(cnt)