import sys;
sys.stdin = open('input.txt','r')

t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    alist=list(map(int,input().split()))
    blist=list(map(int,input().split()))
    na=len(alist)
    nb=len(blist)
    arr=[0]*nb
    for b in range(nb):
        for a in range(na):
            if alist[a]>blist[b]:continue
            else:
                arr[a]+=1
                break
    a=max(arr)
    for i in range(nb):
        if a==arr[i]:
            print('#{} {}'.format(tc,i+1))
