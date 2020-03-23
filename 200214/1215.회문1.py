import sys;
sys.stdin = open('회문.txt','r')

for tc in range(1,11):
    t=int(input())
    que=[]
    for _ in range(8):
        _list=list(map(str,input()))
        que.append(_list)
    print(t,que)
    cnt=0
    for i in range(8):
        if t==6:
            for j in range(2,t-2):
                if que[i][j]==que[i][j+1]:
                    if que[i][j-1]==que[i][j+2]:
                        if que[i][j-2]==que[i][j+3]:
                            cnt+=1
                if que[j][i]==que[j+1][i]:
                    if que[j-1][i]==que[j+2][i]:
                        if que[j-2][i] == que[j+3][i]:
                            cnt+=1
        if t==4:
            for j in range(1,t+2):
                if que[i][j]==que[i][j+1]:
                    if que[i][j-1]==que[i][j+2]:
                        cnt+=1
                if que[j][i]==que[j+1][i]:
                    if que[j-1][i]==que[j+2][i]:
                        cnt+=1
        if t==3:
            for j in range(1,t+4):
                if que[i][j-1]==que[i][j+1]:
                        cnt+=1
                if que[j-1][i]==que[j+1][i]:
                        cnt+=1
        if t==5:
            for j in range(2,t+1):
                if que[i][j-2]==que[i][j+2]:
                    if que[i][j - 1] == que[i][j + 1]:
                        cnt += 1
                if que[j-1][i]==que[j+1][i]:
                    if que[j - 2][i] == que[j + 2][i]:
                        cnt+=1
        if t==7:
            for j in range(3,t-3):
                if que[i][j-2]==que[i][j+2]:
                    if que[i][j - 1] == que[i][j + 1]:
                        if que[i][j-3]==que[i][j+3]:
                            cnt += 1
                if que[j-1][i]==que[j+1][i]:
                    if que[j - 2][i] == que[j + 2][i]:
                        if que[j - 3][i] == que[j + 3][i]:
                            cnt+=1
    print('#{} {}'.format(tc,cnt))






