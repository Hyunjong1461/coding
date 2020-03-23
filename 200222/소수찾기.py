t = int(input())

arr = list(map(int,input().split()))
cnt = 0
flag=0
for i in range(t):
    a = arr[i]
    # print(a)
    if a ==1:
        cnt=cnt
    elif a ==2 :
        cnt+=1
    else:
        for j in range(2,a):
            if a%j==0:

                flag=0
                break
            else:
                flag=1
    if flag == 1:
        cnt+=1
print(cnt)