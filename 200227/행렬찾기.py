import sys;
sys.stdin = open('input.txt','r')

t=int(input())
for tc in range(1,t+1):
    size=int(input())
    que=[]
    que1=[]
    for _ in range(size):
        _list=list(map(int,input().split()))
        que.append(_list)
    print(que)

    cnt1=0
    cnt2=0

    for i in range(size):
        if que[i][j] != 0:
            que1.append([i, j])
    for j in range(size):
        if que[i][j]!=0:
            que1.append([i,j])
    print(que1)























    # for i in range(size):
    #     cntc = 0
    #     for j in range(size):
    #         if que[i][j]==0:
    #             if cntc==0:
    #                 continue
    #             else:
    #                 quecntc.append(cntc)
    #                 cntc=0
    #         if que[i][j]!=0:
    #             cntc+=1
    # print(quecntc)
    # for j in range(size):
    #     cntr = 0
    #     for i in range(size):
    #         if que[i][j]==0:
    #             if cntr==0:
    #                 continue
    #             else:
    #                 quecntr.append(cntr)
    #                 cntr=0
    #         if que[i][j]!=0:
    #             cntr+=1
    # print(quecntr)


