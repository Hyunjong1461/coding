import queue
arr=queue.Queue()
def push(a):
    arr.put(a)
def front():
    if arr.qsize==0:
        print(-1)
    print(arr.queue[0])
def back():
    if arr.qsize==0:
        print(-1)
    print(arr.queue[-1])
def size():
    print(arr.qsize())
def empty():
    if arr.qsize()==0:
        print(1)
    else:
        print(0)
def pop():
    if arr.qsize()==0:
        print(-1)
    else:
        print(arr.get())

t=int(input())
m=[]
for tc in range(1,t+1):
    m.append(input().split())

for i in range(t):
    if m[i][0]=='push':
        push(m[i][1])
    elif m[i][0]=='front':
        front()
    elif m[i][0]=='back':
        back()
    elif m[i][0]=='size':
        size()
    elif m[i][0]=='empty':
        empty()
    elif m[i][0]=='pop':
        pop()