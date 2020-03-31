import copy
import sys
sys.setrecursionlimit(10**6)

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def dfsR(r,c):
    global cnt
    arr[r][c]=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr[nr][nc]=='R':
            dfsR(nr,nc)

def dfsG(r,c):
    global cnt
    arr[r][c]=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr[nr][nc]=='G':
            dfsG(nr,nc)

def dfsB(r,c):
    global cnt
    arr[r][c]=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr[nr][nc]=='B':
            dfsB(nr,nc)

def dfsR1(r,c):
    global cnt
    arr1[r][c]=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr1[nr][nc]=='R':
            dfsR1(nr,nc)

def dfsB1(r,c):
    global cnt
    arr1[r][c]=0
    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i]
        if 0<=nr<t and 0<=nc<t and arr1[nr][nc]=='B':
            dfsB1(nr,nc)



t=int(input())
arr=[]
for i in range(t):
    _list=list(map(str,input()))
    arr.append(_list)

arr1=copy.deepcopy(arr)

cnt=0
for i in range(t):
    for j in range(t):
        if arr[i][j]=='R':
            dfsR(i,j)
            cnt+=1
        if arr[i][j]=='G':
            dfsG(i,j)
            cnt+=1
        if arr[i][j]=='B':
            dfsB(i,j)
            cnt+=1
print(cnt,end=' ')


for i in range(t):
    for j in range(t):
        if arr1[i][j]=='G':
            arr1[i][j]='R'

cnt1=0
for i in range(t):
    for j in range(t):
        if arr1[i][j]=='R':
            dfsR1(i,j)
            cnt1+=1
        if arr1[i][j]=='B':
            dfsB1(i,j)
            cnt1+=1
print(cnt1)