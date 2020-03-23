import sys;
sys.stdin = open('sadari.txt','r')

for tc in range(1,11):
    t= int(input())
    arr=[]
    for i in range(100):
        _list=list(map(int,input().split()))
        arr.append(_list)
    print(arr)
