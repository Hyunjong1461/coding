dr=[0,-1]
dc=[-1,0]

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr = []
    for ii in range(n):
        _list=list(map(int,input().split()))
        arr.append(_list)

    for r in range(n):
        for c in range(n):
            value=[]
            for i in range(2):
                nr=r+dr[i]
                nc=c+dc[i]
                if 0<=nr<n and 0<=nc<n:
                    value.append(arr[nr][nc])
            if value:
                arr[r][c] += min(value)

    print('#{} {}'.format(tc,arr[n-1][n-1]))
