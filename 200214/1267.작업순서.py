import sys;
sys.stdin = open('작업순서2.txt','r')

def dfs ():


for tc in range(1,3):
    M,N=map(int,input().split())
    list_ = list(map(int,input().split()))
    print(list_)
    arr=[[0]*(M+1) for _ in range(M+1)]
    for i in range(2*N):
        if i%2==1:
            arr[list_[i-1]][list_[i]]=1
    print(arr)


    start=[]
    for j in range(M + 1):
        cnt = 0
        for i in range(M + 1):
            if arr[i][j]==1:
                cnt+=1
            else:
                cnt=cnt
        if j>0 and cnt==0:
            start.append(j)

    print(start)



