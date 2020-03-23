x, y ,w,h=map(int,input().split())

x1 = w - x
y1 = h-y
arr=[]
arr.append([x,y,x1,y1])
print(min(arr[0]))