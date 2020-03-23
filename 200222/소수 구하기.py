#에라토스테네스의 체로 다시 풀기
m,n=map(int,input().split())
arr=[]
for i in range(m,n+1):
    if i==1:
        continue
    else:
        arr.append(i)

for i in range(m,n+1):
    for j in range(i+1,len(arr)):
        if arr[i]==-1:
            break
        elif arr[j]%2==0:
            arr[j] = -1
        elif arr[j]%arr[i]==0:
            arr[j] = -1

for k in range(len(arr)):
    if arr[k]!=-1:
        print(arr[k])