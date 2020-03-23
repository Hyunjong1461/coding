arr=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

diff=[(-1,0),(1,0),(0,-1),(0,1)]

for x in range(5):
    for y in range(5):
        sumvalue=0
        for dx, dy in diff:
            tx,ty=x+dx,y+dy
            if 0<=tx<5 and 0<=ty<5:
                sumvalue+=abs(arr[x][y]-arr[tx][ty])
        print(sumvalue,end=' ')
    print()