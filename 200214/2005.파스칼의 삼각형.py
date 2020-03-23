import sys;
sys.stdin = open('pascal.txt','r')

T=int(input())
for i in range(T):
    que=int(input())
    print('#{}'.format(que))

    bin=[[0]*que for _ in range(que)]

    for k in range(que):
        bin[k][0]=1
        bin[k][k]=1
        if k >= 2:
            for i in range(1,que):
                bin[k][k-i]=bin[k-1][k-i]+bin[k-1][k-i-1]
    # print(bin)
    for i in range(que):
        for j in range(que):
            if bin[i][j]!=0:
                print(bin[i][j],end=' ')
        print()