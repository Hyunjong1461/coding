import sys;
sys.stdin = open('input.txt','r')

# def dfs(i,j,arr):
#     global cnt,ans
#     if i==x and j==x:
#         return cnt
#     else:
#         while 1:
#             if i+1<x and j+1<x:
#                 if arr[i+1][j]==arr[i][j]+1:
#                     i+=1
#                     cnt+=1
#                     dfs(i,j,arr)
#                 elif arr[i][j+1]==arr[i][j]+1:
#                     j+=1
#                     cnt+=1
#                     dfs(i,j,arr)
#                 else:
#                     # dfs(i,j)
#                     ans.append(cnt)
#                     break
#
#
#
#
# t=int(input())
#
# for i in range(t):
#     arr=[]
#     ans=[]
#     cnt=0
#     x=int(input())
#     for j in range(x):
#         _list=list(map(int,input().split()))
#         arr.append(_list)
#     print(dfs(0,0,arr))
