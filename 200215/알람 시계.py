h,m = map(int,input().split())

if m>=45:
    m=m-45
    if m!=0:
        print('{} {}'.format(h,m))
    elif m==0:
        print('{}'.format(h))

elif m<45:
    m=60-(45-m)
    h=h-1
    if h==-1:
        h=23
    print('{} {}'.format(h, m))