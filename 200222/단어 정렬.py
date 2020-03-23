t=int(input())
arr=[]
arr2=[]
for i in range(t):
    k=str(input())
    arr.append(k)
    arr2.append(len(k))
print(arr,arr2)
arr3=sorted(arr2)
arr4=[]
visit=[]
for i in range(t):
    for j in range(t):
        if arr2[j]==arr3[i]:
            if j not in visit:
                arr4.append(arr[j])
                visit.append(j)
print(arr4)

print(ans)