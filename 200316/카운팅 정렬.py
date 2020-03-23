arr=[0,4,1,3,1,2,4,1]
count=[0]*(max(arr)+1)
b=[0]*len(arr)
for i in arr:
    count[i]+=1
print(count)
for j in range(len(count)):
    if j==0:
        count[j]=count[j]
    else:
        count[j]+=count[j-1]
print(count)

for i in arr:
    count[i]-=1
    b[count[i]]=i
print(b)
