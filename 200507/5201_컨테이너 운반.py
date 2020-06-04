t=int(input())

for tc in range(1,t+1):
    n,m=map(int,input().split())
    container=sorted(list(map(int,input().split())))
    bus=sorted(list(map(int,input().split())))
    ans=[]

    # print(n,m,container,bus)
    flag=True
    cnt=0
    while flag:
        if len(bus)==0:
            break
        a=bus.pop()
        for i in range(n-1,-1,-1):
            if container[i] <=a:
                cnt+=container[i]
                container[i]=10000000
                break
        container=sorted(container)

    print('#{} {}'.format(tc,cnt))