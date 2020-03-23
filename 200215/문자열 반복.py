t=int(input())

for i in range(t):
    m,n=map(str,input().split())
    m1=int(m)
    for j in range(len(n)):
        for i in range(m1):
            print(n[j],end='')
    print()
