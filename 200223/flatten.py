import sys;
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    t=int(input())
    arr=list(map(int,input().split()))

    for i in range(t):
        arr=sorted(arr)
        arr[-1]=arr[-1]-1
        arr[0]=arr[0]+1
    arr1=sorted(arr)
    print('#{} {}'.format(tc,arr1[-1]-arr1[0]))