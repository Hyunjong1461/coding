n=5

arr=[[0]*n for _ in range(n)]

row_start = col_start = 0
row_end = col_end =n-1

cnt=1

while row_start<=row_end and col_start<=col_end:
        for i in range(col_start, col_end + 1):
            arr[row_start][i] = cnt
            cnt += 1
        row_start += 1

        for i in range(row_start, row_end + 1):
            arr[i][col_end] = cnt
            cnt += 1
        col_end -= 1

        for i in range(col_end, col_start - 1, -1):
            arr[row_end][i] = cnt
            cnt += 1
        row_end -= 1

        for i in range(row_end, row_start - 1, -1):
            arr[i][col_start]=cnt
            cnt+=1
        col_start+=1

print(arr)