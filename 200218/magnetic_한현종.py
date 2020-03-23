for tc in range(1,11):
    t=int(input())
    que=[]
    for i in range(100):
        _list=list(map(int,input().split()))
        que.append(_list)
    # print(t,que)#t넣기

# 자석 바꾸기

    for j in range(len(que[0])):
        i = 0
        while 1:
            if i<len(que[0]):
                if que[i][j]==2:
                    que[i][j]=0
                    i=i+1
                elif que[i][j]==0:
                    i=i+1
                elif que[i][j]==1:
                    break
            else:
                break
        i=0
        while 1:
            if i > -len(que[0]):
                if que[i-1][j] == 1:
                    que[i-1][j] = 0
                    i = i - 1
                elif que[i-1][j] == 0:
                    i = i - 1
                elif que[i-1][j] == 2:
                    break
            else:
                break

    #자석 수 세기
    cnt=0
    for j in range(len(que[0])):
        for i in range(len(que[0])):
            for k in range(i+1,len(que[0])):
                if que[i][j]==1 and que[k][j]==2:
                    cnt += 1
                    for u in range(i,k+1):
                        que[u][j]=0

    print('#{} {}'.format(tc,cnt))
