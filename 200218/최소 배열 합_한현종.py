def minsum(n,a,arr):
    global result
    global visit
    global min
    if result >min:
        return
    if n==a:
        if min > result:
            min = result
        return min
    else:
        for i in range(a):
            if i not in visit:
                result+=arr[n][i]
                visit.append(i)
                minsum(n+1,a,arr)
                visit.pop()
                result-=arr[n][i]



t= int(input())
sum1=[]
for tc in range(1,t+1):
    a= int(input())
    arr = []
    for _ in range(a):
        _list=list(map(int,input().split()))
        arr.append(_list)
    # print(arr)
    result=0
    visit=[]
    min = 999999
    minsum(0,a,arr)
    print('#{} {}'.format(tc,min))