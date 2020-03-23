import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[[0]*10 for _ in range(10)]
    cnt=0
    for ii in range(n):
        _list=list(map(int,input().split()))
        for i in range(_list[0],_list[2]+1):
            for j in range(_list[1],_list[3]+1):
                arr[i][j]+=_list[4]
                if arr[i][j]==3:
                    cnt+=1
    print('#{} {}'.format(tc,cnt))
