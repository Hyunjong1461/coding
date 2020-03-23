arr=[7,4,2,0,0,6,0,7,0]
n=len(arr)

ans=0
for i in range(n):
    h = n-1-i
    if ans>=h:break
    for j in range (i+1,n):
        if arr[i]<=arr[j]:
            h-=1
    print(h)
    ans=max(ans,h)
print(ans)