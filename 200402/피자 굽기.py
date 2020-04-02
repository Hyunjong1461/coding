t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    ans=[]
    r=-1

    while 1:#피자 행렬만들기
        if r==n-1:break
        r+=1
        ans.append((r,arr[r]))



    while 1: #요기부터 중요
        if len(ans)==1: break
        i,j=ans.pop(0)
        j=j//2
        if j==0:
            if r<m-1:
                r+=1
                ans.append((r,arr[r]))
        if j!=0:
            ans.append((i,j))
    print('#{} {}'.format(tc,ans[0][0]+1))