import sys;
sys.stdin = open('input.txt','r')

for tc in range(1,11):
    t=int(input())
    arr=list(map(int,input().split()))
    cnt=0
    for i in range(2,t-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i-2] and arr[i]>arr[i+1] and arr[i]>arr[i+2]:
            cnt+=min(arr[i]-arr[i-1],arr[i]-arr[i-2],arr[i]-arr[i+1],arr[i]-arr[i+2])

    print('#{} {}'.format(tc,cnt))