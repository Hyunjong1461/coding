def su (l,r):

    if l==r:
        return l

    ls=su(l,(l+r)//2)
    rs=su((l+r)//2+1,r)
    return game(ls,rs)

def game(l,r):
    if que[l-1]==1 and que[r-1]==2:
        return r
    if que[l-1]==2 and que[r-1]==3:
        return r
    if que[l-1]==3 and que[r-1]==1:
        return r
    if que[l-1]==2 and que[r-1]==1:
        return l
    if que[l-1]==3 and que[r-1]==2:
        return l
    if que[l-1]==1 and que[r-1]==3:
        return l
    if que[l-1]==que[r-1]:
        return l

t=int(input())
for tc in range(1,t+1):
    a=int(input())
    que=list(map(int,input().split()))
    print('#{} {}'.format(tc,su(1,a)))