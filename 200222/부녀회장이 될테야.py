T=int(input())

for _ in range(T):
    m=int(input())
    n=int(input())

    arr=[[0]*14 for _ in range(15)]
    # print(arr)
    for i in range(1,15):
        arr[0][i-1]=i
    # print(arr)

    for j in range(1,15):
        for i in range(len(arr[0])):
            for k in range(0,i+1):
                arr[j][i]+=arr[j-1][k]
    print(arr[m][n-1])