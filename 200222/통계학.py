import math;
t=int(input())
na=[]
arr=[]
ans=[]
for ii in range(t):
    c=int(input())
    arr.append(c)
arr2=sorted(arr)
# print(arr2)
print(math.floor(sum(arr2)/len(arr2)))
print(arr2[len(arr2)//2])


for i in range(len(arr)):
    cnt = 0
    for j in range(i + 1, len(arr)):
        if arr2[i] == arr2[j]:
            cnt += 1
    na.append(cnt)

for i in range(len(na)):
    if na[i]==max(na):
        ans.append(i)

if len(ans)>=2:
    print(arr2[ans[1]])
else:
    print(arr2[ans[0]])

print(arr2[-1]-arr2[0])