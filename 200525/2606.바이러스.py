nn=int(input())
t=int(input())
arr=[]
for i in range(t):
    m,n=map(int,input().split())
    arr.append((m,n))


stack=[]
visited=[0]*(nn+1)

stack.append(1)
while stack:
    a=stack.pop()
    for i in range(t):
        for j in range(2):
            if a == arr[i][j]:
                if visited[a]!=1:
                    if j ==1:
                        stack.append(arr[i][0])
                    else:
                        stack.append(arr[i][1])
    visited[a]=1
count=0
for i in range(len(visited)):
    if visited[i]==1:
        count+=1
print(count-1)

