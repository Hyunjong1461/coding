arr=[]
for i in range(9):
    i = int(input())
    arr.append(i)
# print(arr)
max=0
cnt=0
for i in range(9):
    if arr[i]>max:
        max=arr[i]
        cnt=i
print(max)
print(cnt+1)