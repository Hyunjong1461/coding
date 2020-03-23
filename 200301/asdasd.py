def minsum(n,a,arr):
    global result
    global visit
    global arr1
    if n==a:
        # global ans
        # ans = min(ans, sum(result))
        arr1.append(sum(result))
        print(*visit)
        # if len(arr1)==a*(a-1):
        # print(arr1)
    else:
        for i in range(a):
            if i not in visit:
                result.append(arr[n][i])
                visit.append(i)
                minsum(n+1,a,arr)
                visit.pop()
                result.pop()



t= int(input())
sum1=[]
for tc in range(1,t+1):
    a= int(input())
    arr = []
    for _ in range(a):
        _list=list(map(int,input().split()))
        arr.append(_list)
    result=[]
    visit=[]
    arr1=[]
    minsum(0, a, arr)
    print(arr1)
