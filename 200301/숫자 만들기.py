import sys;
sys.stdin = open('input.txt','r')

def back(i,sum):
    global arr
    if i==n:
        arr.append(sum)


    for j in range(len(sachic)):
        if sachic[j]>0:
            if j==0:
                sachic[0]-=1
                back(i+1,sum+number[i])
                sachic[0] += 1
            if j==1:
                sachic[1] -= 1
                back(i + 1, sum - number[i])
                sachic[1] += 1
            if j==2:
                sachic[2] -= 1
                back(i+1,sum*number[i])
                sachic[2] += 1
            if j==3:
                sachic[3] -= 1
                back(i+1,int(sum/number[i]))
                sachic[3] += 1

t=int(input())

for tc in range(1,t+1):
    n=int(input())
    sachic=list(map(int,input().split()))
    number=list(map(int,input().split()))
    arr=[]
    back(1,number[0])
    print('#{} {}'.format(tc,max(arr)-min(arr)))