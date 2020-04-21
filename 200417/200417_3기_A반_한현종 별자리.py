import sys;
sys.stdin=open('input.txt','r')

from _collections import deque

dr=[1,-1,0,0,1,-1,1,-1]
dc=[0,0,1,-1,1,-1,-1,1]
t=int(input())

for tc in range(1,t+1):
    arr=[]
    for i in range(10):
        alist=list(map(int,input().split()))
        arr.append(alist)

    Q=deque()
    visit=[]
    cnt=0
    for i in range(10):
        for j in range(10):
            if arr[i][j]==1:
                Q.append((i,j))
                cnt+=1
                while Q:
                    q=Q.popleft()
                    arr[q[0]][q[1]]=0
                    visit.append(q)
                    for ii in range(8):
                        nr = q[0]+dr[ii]
                        nc = q[1]+dc[ii]
                        if 0<=nr<10 and 0<=nc<10:
                            if arr[nr][nc]==1:
                                Q.append((nr,nc))
    print('#{} {}'.format(tc,cnt))