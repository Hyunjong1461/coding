arr1=[]
arr2=[]
for ii in range(3):
    m,n=map(int,input().split())
    arr1.append(m)
    arr2.append(n)

if arr1[0]==arr1[1]:
    print(arr1[2],end=' ')
if arr1[1]==arr1[2]:
    print(arr1[0],end=' ')
if arr1[0]==arr1[2]:
    print(arr1[1],end=' ')

if arr2[0]==arr2[1]:
    print(arr2[2])
if arr2[1]==arr2[2]:
    print(arr2[0])
if arr2[0]==arr2[2]:
    print(arr2[1])


