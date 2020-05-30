t = int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[]
    for _ in range(n):
        _list=list(map(int,input().split()))
        arr.append(_list)
    print(arr)

    visited=[0]*n

    