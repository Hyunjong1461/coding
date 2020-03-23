import sys;
sys.stdin = open('input.txt','r')

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[]
    for i in range(n):
        _list=list(map(int,input().split()))
        arr.append(_list)

    # print(arr)
    num=len(arr)

    arr1=[0]*400

    for i in range(num):
        if arr[i][0]+1==arr[i][1]:
            continue;
        elif arr[i][0]>arr[i][1]:
            for j in range(arr[i][0],arr[i][1]+1):
                arr1[j]+=1
        else:
            for j in range(arr[i][1],arr[i][0]-1,-1):
                arr1[j]+=1
    print('#{} {}'.format(tc,max(arr1)))