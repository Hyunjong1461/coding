arr=[55,7,78,12,42]

for j in range(len(arr)-1,0,-1):
    for i in range(0,j):
        if arr[i]>=arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)