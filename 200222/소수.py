m=int(input())
n=int(input())


cnt=0
flag=0
sum=0
arr=[]
for i in range(m,n+1):
    a = i
    # print(a)
    if a ==1:
        continue
    elif a ==2 :
        flag =1
        arr.append(a)
    else:
        for j in range(2,a):
            if a%j==0:
                flag=0
                break
            else:
                flag=1
    if flag == 1:
        sum+=i
        arr.append(i)
if sum !=0:
    print(sum)
    print(min(arr))
else:
    print(-1)