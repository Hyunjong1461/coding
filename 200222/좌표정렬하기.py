t=int(input())
arr=[]
for i in range(t):
    a,b=map(int,input().split())
    arr.append([b,a])
# print(arr)

arr2=sorted(arr)
for i in range(t):
    print('{} {}'.format(arr2[i][1],arr2[i][0]))