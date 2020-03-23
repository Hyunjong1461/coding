def self_number(que):
    arr=[]
    for i in range(1,que+1):
        arr.append(i)
    # print(arr)
    ans2=[]
    for k in range(1,que+1):
        sum=0
        str1=str(k)
        b=0
        for i in range(len(str1)):
            b+=int(str1[i])
            sum=k+b
        ans2.append(sum)
    # print(ans2)
    for x in range(len(arr)):
        if arr[x] not in ans2:
            print(arr[x])

self_number(10000)

