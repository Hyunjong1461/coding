import sys;
sys.stdin = open('input.txt','r')

nr=[0,0,0,1,1,1,-1,-1,-1]
nc=[-1,0,1,-1,0,1,-1,0,1]



t=int(input())

for tc in range(1,t+1):
    arr=[]
    for i in range(9):
        alist=list(map(int,input().split()))
        arr.append(alist)

    # print(arr)
    arr1=[1,2,3,4,5,6,7,8,9]
    flag=1
    for i in range(9):
        if sorted(arr[i])==arr1:continue
        else:
            flag = 0
            break

    for i in range(9):
        prac=[]
        for j in range(9):
            prac.append(arr[j][i])
        pracsort=sorted(prac)
        if pracsort==arr1:continue
        else:
            flag=0
            break
    i=0
    j=0
    for r in range(1,8,3):
        for c in range(1,8,3):
            prac = []
            for k in range(9):
                i=r+nr[k]
                j=c+nc[k]
                prac.append(arr[i][j])
            pracsort=sorted(prac)
            if pracsort == arr1:
                continue
            else:
                flag = 0
                break
    print('#{} {}'.format(tc,flag))