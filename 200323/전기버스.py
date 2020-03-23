import sys;
sys.stdin = open('input.txt','r')

t = int(input())

for tc in range(1,t+1):
    K,N,M=map(int,input().split())
    alist=list(map(int,input().split()))
    # print(K,N,M)
    # print(alist)

    startpoint=0
    cnt=0
    sub=[]
    for i in range(M):
        if M==0:
            sub.append(alist[0])
        else:
            sub.append(alist[i]-alist[i-1])

    for i in range(M):
        if sub[i]>K:
            print('#{} 0'.format(tc))
            break
    else:
        while 1:
            if startpoint+K>=N:
                break
            elif startpoint+K in alist:
                cnt+=1
                startpoint+=K
            else:
                startpoint-=1
        print('#{} {}'.format(tc,cnt))
