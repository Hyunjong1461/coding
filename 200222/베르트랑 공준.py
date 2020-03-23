def sosu(n):
    flag=0
    arr=[]
    cnt=0
    for i in range(n+1,2*n+1):
        if i==1:
            cnt=cnt
        elif i ==2 :
            flag =1
            cnt+=1
        else:
            for j in range(2,i):
                if i%j==0:
                    flag=0
                    break
                else:
                    flag=1
            if flag == 1:
                cnt+=1
    print(cnt)

while 1:
    n=int(input())
    if n==0:
        break
    sosu(n)