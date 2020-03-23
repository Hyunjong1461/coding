t=int(input())
_list=list(map(int,input().split()))
# print(_list)
# print(max(_list))
arr=[]
for i in range(t):
    arr.append((_list[i]/max(_list))*100)
# print(arr)
sum=0
for j in range(len(arr)):
    sum+=arr[j]
print(sum/t)