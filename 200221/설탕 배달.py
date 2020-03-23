N=int(input())
i=0
flag = False
while 1:
    a5= N-3*i
    if a5>=0 and a5%10 == 5:
        flag=True
        break
    elif a5>=0 and a5%10 ==0:
        flag = True
        break
    elif a5<0:
        print(-1)
        break
    else:
        i+=1
if flag==True:
    print((a5//5)+i)
