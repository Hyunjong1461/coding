from _collections import deque

Q=deque()
arr=deque()
t,cnt=map(int,input().split())
for i in range(1,t+1):
    Q.append(i)

while len(Q)>0:
    for i in range(cnt-1):
        Q.append(Q.popleft())
    arr.append(Q.popleft())

print('<',end='')
for i in range(t-1):
    print(arr[i],end=', ')
print(arr[-1],end='')
print('>')