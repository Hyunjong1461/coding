t=int(input())
for i in range(t):
    str1=list(map(str,input()))
    # print(str1)
    arr=[0]*len(str1)
    cnt=0
    for i in range(len(str1)):
        if str1[i]=='O':
            cnt+=1
            arr[i]=cnt
        elif str1[i]=='X':
            cnt=0
            arr[i] = cnt
    print(sum(arr))
