t = int(input())

for tc in range(1,t+1):
    n=int(input())
    nlist=list(map(int,input().split()))

    maxvalue=0
    for i in range(len(nlist)):
        for j in range(i+1,len(nlist)):
            a=str(nlist[i]*nlist[j])
            flag=1
            for x in range(len(a)):
                for y in range(x+1,len(a)):
                    if a[x]>a[y]:
                        flag=0
                        break
            if flag==1:
                if int(a)>maxvalue:
                    maxvalue=int(a)

    if maxvalue==0:
        print('#{} -1'.format(tc))
    else:
        print('#{} {}'.format(tc,maxvalue))
