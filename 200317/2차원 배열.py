arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(arr)

#행 우선 순회

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')

print()

#열 우선 순회

for i in range(len(arr[0])):
    for j in range(len(arr)):
        print(arr[j][i],end=' ')

print()
#지그재그 순회

for i in range(len(arr)):
    # if i%2==0:
    #     for j in range(len(arr[i])):
    #         print(arr[i][j], end=' ')
    # else:
    #     for j in range(len(arr[i])-1,-1,-1):
    #         print(arr[i][j], end=' ')
    for j in range(len(arr[0])):
        print(arr[i][j+(-2*j-1)*(i%2)],end=' ')
print()

#델타를 이용한 탐색

#x:행 , y:열
#상, 하 , 좌, 우
# dx= [1,-1,0,0]
# dy = [0,0,-1,1]
diff=[(-1,0),(1,0),(0,-1),(0,1)]


for x in range(len(arr)):
    for y in range(len(arr[0])):
        # for i in range(4):
        #     testx = x + dx[i]
        #     testy = y + dy[i]
        for dx, dy in diff:
            testx,testy =x+dx,y+dy
            if 0<=testx<3 and 0<=testy<4:
                print(arr[testx][testy],end=' ')
        print()
#x:행 , y:열
#상, 하 , 좌, 우


#전치행렬

arr1=[[1,2,3],[4,5,6],[7,8,9]]


for i in range(len(arr1)):
    for j in range(len(arr1)):
        if i<j:
            arr1[i][j]=arr1[j][i]
print(arr1)



