from _collections import deque

t=int(input())

for i in range(t):
    strlist=list(map(str,input()))
    Q = deque()
    n=int(input())
    alist=input()
    alist=alist[1:-1].split(',')
    if n>0:
        for i in alist:
            Q.append(int(i))

    flag=True
    cnt=0
    for i in range(len(strlist)):
        if strlist[i]=='R':
            cnt+=1
        if strlist[i]=='D':
            if cnt%2==0:
                if Q :
                    Q.popleft()
                elif not Q:
                    flag=False
            elif cnt%2==1:
                if Q:
                    Q.pop()
                elif not Q:
                    flag = False
    if cnt % 2 == 1:
        Q.reverse()


    ans=[]
    if flag==False:
        print('error')
    else:
        print('[', end='')
        if Q:
            for i in range(len(Q)-1):
                print('{}'.format(Q[i]),end=',')
            print(Q[-1],end='')
        print(']')

