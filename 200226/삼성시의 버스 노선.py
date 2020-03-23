import sys;
sys.stdin = open('input.txt','r')


t = int(input())

for tc in range(1,t+1):
    arr = []
    arr2 = []
    n=int(input())
    for i in range(n):
        a, b =map(int,input().split())
        for _list in range(a,b+1):
            arr.append(_list)
    k = int(input())
    for j in range(k):
        cnt=0
        tt=int(input())
        for size in range(len(arr)):
            if tt ==arr[size]:
                cnt+=1
        arr2.append(cnt)
    print('#{} '.format(tc),end='')
    for i in range(len(arr2)):
        print('{}'.format(arr2[i]),end=' ')
    print()
