import sys;
sys.stdin = open('pascal.txt','r')

T=int(input())

for i in range(1,T+1):
    a=int(input())
    sum = 0
    for i in range(1,a+1):
        if i%2!=0:
            sum+=i
        else:
            sum-=i
    print('#{} {}'.format(i,sum))
