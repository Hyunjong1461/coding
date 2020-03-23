import sys;
sys.stdin = open('input.txt','r')

visit=[0]*12
def back(i=0,sum=0):
    global arr
    if i>=12:
        arr.append(sum)
    else:
        back(i+1,sum+plan[i]*price[0])
        back(i+1,sum+price[1])
        back(i+3, sum+price[2])
        back(i+12, sum+price[3])

t=int(input())
for tc in range(1,t+1):
    cnt = 0
    # day,month,month3,year = map(int,input().split())
    price =list(map(int,input().split()))
    plan=list(map(int,input().split()))
    arr=[]
    back()
    print('#{} {}'.format(tc,min(arr)))