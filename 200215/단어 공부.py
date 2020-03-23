t=str(input())

s=t.upper()
a=s
dicready=list(set(a))
dic={}
for i in dicready:
    dic[i]=0
for i in range(len(a)):
    for x, y in dic.items():
        if x in a[i]:
            dic[x]+=1
value=[]
maxvalue=0
for x in dic.keys():
    if dic[x]>=maxvalue:
        maxvalue=dic[x]
arr=[]
for i in dic.keys():
    if dic[i]==maxvalue:
        arr.append(i)

if len(arr)>=2:
    print('?')
else:
    print(arr[0])





#32
#97 =>a
#65 =>A