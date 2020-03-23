t=int(input())
arr=[]
for i in range(t):
    k = int(input())
    arr.append(k)
# print(arr)
arr2=[]
for i in range(t):
    if arr[i]!=0:
        arr2.append(arr[i])
    else:
        arr2.pop()
print(sum(arr2))