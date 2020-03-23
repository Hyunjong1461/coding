t= int(input())
arr=[]
for i in range(t):
    _list=list(map(str,input().split()))
    arr.append(_list)

for i in range(t):
    for j in range(t-1):
        if arr[j][0]!=arr[j+1][0]:
            if arr[j][0]>arr[j+1][0]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

for i in range(t):
    print('{} {}'.format(arr[i][0],arr[i][1]))