arr=[]
for _ in range(10):
    i = int(input())
    arr.append(i%42)
arr1=sorted(arr)
arr2=list(set(arr1))
print(len(arr2))