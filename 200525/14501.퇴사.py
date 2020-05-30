t=int(input())
arr1=[]

for i in range(t):
    m,n=map(int,input().split())
    arr1.append((m,n))

print(arr1)
maxvalue=0
day=0
while day<=t-1:
    maxvalue+=arr1[day][1]
    day+=
