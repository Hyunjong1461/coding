n,x=map(int,input().split())
_list=list(map(int,input().split()))

for i in range(n):
    if _list[i]<x:
        print(_list[i],end=' ')