t=int(input())
arr1=[]
ans=[]
for i in range(t):
    arr=list(map(int,input().split()))
    arr1.append(arr)
# print(arr1)

for i in range(t):
    cnt=1
    for j in range(t):
        if i!=j:
            if arr1[i][0]<arr1[j][0]:
                if arr1[i][1]<arr1[j][1]:
                    cnt+=1
    ans.append(cnt)
for i in range(t):
    print(ans[i],end=' ')