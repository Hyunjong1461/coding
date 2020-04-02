

t=int(input())
for tc in range(1,t+1):
    a,b,c,d=map(int,input().split())
    arr=list(map(int,input().split()))
    ans1=[0]*12
    ans2=[b]*12
    ans3=[c]*12
    for i in range(12):
        ans1[i]=arr[i]*a

    for i in range(12):
        if ans1[i]<ans2[i]:continue
        else:
            ans1[i]=ans2[i]


    for i in range(12):
        if ans1[i]!=0:
            if 0 <= i < 10:
                if sum(ans1[i:i+3])>ans3[i]:
                    ans1[i]=ans3[i]
                    ans1[i+1]=0
                    ans1[i+2]=0
            elif i==10:
                if sum(ans1[i:i + 2]) > ans3[i]:
                    ans1[i] = ans3[i]
                    ans1[i + 1] = 0
            else:
                if sum(ans1[i:i + 1]) > ans3[i]:
                    ans1[i] = ans3[i]
    print(ans1)
    if sum(ans1)>d:
        print('#{} {}'.format(tc,d))
    else:
        print('#{} {}'.format(tc,sum(ans1)))


