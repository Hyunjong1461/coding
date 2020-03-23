t= int(input())
for tc in range(1,t+1):
    str=input()
    n=len(str)
    alist = [0]*(n//3)
    for i in range(n//3):
        alist[i]=str[3*i:3*i+3]
    SDHC=[13,13,13,13]
    flag=1
    for i in range(len(alist)):
        for j in range(i+1,len(alist)):
            if alist[i]==alist[j]:
                flag=False
                break
    if flag!=False:
        for k in range(len(alist)):
            if 'S' in alist[k]:
                SDHC[0]-=1
            elif 'D' in alist[k]:
                SDHC[1]-=1
            elif 'H' in alist[k]:
                SDHC[2]-=1
            elif 'C' in alist[k]:
                SDHC[3]-=1
        print('#{}'.format(tc),end=' ')
        print(*SDHC)
    else:
        print('#{} ERROR'.format(tc))