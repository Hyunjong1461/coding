import sys;
sys.stdin = open('sosinsu.txt','r')

T=int(input())

for i in range(T):
    a=int(input())
    cnt2=0
    cnt3=0
    cnt5=0
    cnt7=0
    cnt11=0
    while 1:
        if a%2==0:
            cnt2+=1
            a=int(a/2)
            if a%2!=0:
                break
        else:
            break
    while 1:
        if a%3==0:
            cnt3+=1
            a=int(a/3)
            if a%3!=0:
                break
        else:
            break
    while 1:

        if a%5==0:
            cnt5+=1
            a=int(a/5)
            if a%5!=0:
                break
        else:
            break
    while 1:
        if a%7==0:
            cnt7+=1
            a=int(a/7)
            if a%7!=0:
                break
        else:
            break
    while 1:
        if a%11==0:
            cnt11+=1
            a=int(a/11)
            if a%11!=0:
                break
        else:
            break
    print('#{} {} {} {} {} {}'.format(i+1,cnt2,cnt3,cnt5,cnt7,cnt11))
