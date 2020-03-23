a=int(input())
b=int(input())
c=int(input())

str1=str(a*b*c)
arr=[]
for i in range(len(str1)):
    arr.append(int(str1[i]))
# print(arr)

ans=[0]*10

for i in range(10):
    cnt = 0
    for j in range(len(arr)):
        if i== arr[j]:
            cnt+=1
            ans[i]=cnt
    print(ans[i])