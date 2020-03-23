N, M = map(int, input().split())
visit = [0] * (N+1)
order = []

def backtrack(k):
    if k == M:
        print(*order)
        print(visit)
    else:
        for i in range(1,N+1):
            if visit[i]: continue
            visit[i] = 1
            order.append(i)
            backtrack(k + 1)
            order.pop()
            visit[i] = 0
backtrack(0)