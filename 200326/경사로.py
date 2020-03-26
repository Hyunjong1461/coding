n,l=map(int,input().split())
listb=[]
for i in range(n):
    lista=list(map(int,input().split()))
    listb.append(lista)

print(listb)

for i in range(n):
    cnt=0
    for j in range(n):
        if 0<=j+1<=n-1:
            if listb[i][j+1] < listb[i][j]:
                for a in range(j+1,j+1+l):
                    if 0<=a<n:
                        listb[i][a]+=1
            if listb[i][j+1] > listb[i][j]:
                for a in range(j,j-l,-1):
                    if 0<=a<n:
                        listb[i][a]+=1
print(listb)

