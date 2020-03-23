t = int(input())
for i in range(t):
    _list=list(map(int,input().split()))
    a=_list.pop(0)
    cnt=0
    for j in range(len(_list)):
        if _list[j]>(sum(_list)/a):
            cnt+=1
    print('%.3f'%(cnt/len(_list)*100),end='')
    print('%')