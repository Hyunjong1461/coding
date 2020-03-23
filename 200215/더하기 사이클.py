i = int(input())
que=i
cnt=0
while 1:
    a= i//10
    b= i%10
    i=(a+b)%10+b*10
    cnt+=1
    if i==que:
        break
print(cnt)

