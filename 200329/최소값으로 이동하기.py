import sys;
sys.stdin = open('input.txt','r')

nr=[1,-1,0,0,1,-1]
nc=[0,0,1,-1,1,-1]

t=int(input())

for tc in range(1,t+1):
    w,h,n=map(int,input().split())

    arr=[[0]*(h+1) for _ in range(w+1)]
    cnt=1
    for nc in range(1,n+1):
        x,y=map(int,input().split())
        arr[x][y]=cnt
        cnt+=1
    print(arr)
        #가로 세로 바꿔서 보기
