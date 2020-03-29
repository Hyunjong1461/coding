import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=str(input())
    m=str(input())
    nn=len(n)
    mn=len(m)
    flag=0
    for i in range(mn):
        if n==m[i:i+nn]:
            flag=1
    print('#{} {}'.format(tc,flag))