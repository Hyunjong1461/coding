m,n = map(int,input().split())

alist=sorted(list(map(str,input().split())))

visited=[0]*n
visit=[]
arr=[]
que=['a','e','i','o','u']


def dfs(a):
    if len(arr)==m:
        cntque=0
        cntnotque=0
        for i in range(len(arr)):
            if arr[i] in que:
                cntque+=1
            else:
                cntnotque+=1
        if cntque>0 and cntnotque>1:
            for i in range(len(arr)):
                print(arr[i],end='')
                visit.append(sorted(arr))
            print()

    else:
        for i in range(n):
            if visited[i]==1:continue
            if len(arr)==0:
                visited[i] = 1
                arr.append(alist[i])
                dfs(a + 1)
                arr.pop()
                visited[i] = 0
            else:
                if alist[i]>arr[-1]: #백트래킹 arr에 저장되있는 마지막보다 들어갈 값이 클 때 만 ㄱㄱ
                    visited[i] = 1
                    arr.append(alist[i])
                    dfs(a + 1)
                    arr.pop()
                    visited[i] = 0

dfs(0)