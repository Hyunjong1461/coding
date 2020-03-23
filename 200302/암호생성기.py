import sys;
sys.stdin = open('input.txt','r')





for tc in range(1,11):
    t=input()
    que=list(map(int,input().split()))

    while 1:
        if que[-1] <= 0:
            que[-1] = 0
            break
        for i in range(5):
            if que[-1] <= 0:
                break
            elif que[0] != 0:
                que[0] = que[0] - i - 1
                que.append(que.pop(0))
    print('#{} '.format(t),end='')
    print(*que)
