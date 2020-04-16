t=int(input())

for tc in range(t):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    for i in range(m):
        arr.append(arr.pop(0))
    print('#{} {}'.format(tc+1,arr[0]))