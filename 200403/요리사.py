import sys
sys.stdin = open('input.txt','r')

t= int(input())

for i in range(t):
    a=int(input())
    arr=[]
    for i in range(a):
        _list=list(map(int,input().split()))
        arr.append(_list)
    # print(arr)
    que=[]
    for i in range(a):
        for j in range(a):
            if i>j:
                que.append((arr[i][j]+arr[j][i],(i,j)))
    print(que)
    n=len(que)
    visit = [0]*n

    minvalue=1000000
    for i in range(n):
        for j in range(i+1,n):
            if minvalue>abs(que[i][0]-que[j][0]):
                if que[i][1][0]!=que[j][1][0]:
                    if que[i][1][1] != que[j][1][0]:
                        if que[i][1][0] != que[j][1][1]:
                            if que[i][1][1] != que[j][1][1]:
                                minvalue=abs(que[i][0]-que[j][0])
    print(minvalue)
