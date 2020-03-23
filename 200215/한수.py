def 한수 (a):
    cnt=0
    for i in range(1,a+1):
        str1=str(i)
        arr=[]
        for j in range(len(str1)):
            arr.append(int(str1[j]))
        if len(arr)<=2:
            cnt+=1
        elif len(arr)==3:
            for k in range(len(str1)-2):
                if arr[k]-arr[k+1]==arr[k+1]-arr[k+2]:
                    cnt+=1
    return cnt

t=int(input())
print(한수(t))
