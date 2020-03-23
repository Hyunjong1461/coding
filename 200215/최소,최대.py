n=int(input())

_list=list(map(int,input().split()))
arr=sorted(_list)
print('{} {}'.format(arr[0],arr[-1]))
