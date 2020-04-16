from _collections import deque

V,E = map(int,input().split())
G = [[] for _ in range(V+1)]

for i in range(E):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)


# 너비 우선 탐색, 시작점 = 1
# 그래프 = 인접리스트 G, 방문정보 표시 (정점의 수만큼 1~V), 큐

visit=[False]*(V+1)
D=[0]*(V+1) # 시작점에서 다른 정점들까지 최단거리 저장
Q=deque()


# 시작점을 방문하고 큐에 저장
visit[1]=True
Q.append(1)
D[1]=0


# 빈큐가 아닐 동안 반복
while Q:
    # 큐에서 정점을 하나 가져온다. -->v
    v=Q.popleft()
    # v의 방문하지 않은 인접정점(w)을 찾아서 방문하고 큐에 저장
    for w in G[v]:
        if not visit[w]:
            visit[w]=True
            Q.append(w)
            D[w]=D[v] + 1
print(D,Q,visit,G)


#너비 우선 탐색
# 큐를 사용한다
# 방문한 정점을 기록하거나, 방문할 정점을 기록
# 시작점에서 가장 가까운 정점들을 모두 방문한다.
#                        (시작점의 인접정점들)
# 시작점에서 거리가 1인 정점을 찾고, 거리가 2인 정점들 찾고, ...
# 깊이 우선 탐색과 같이 시작점에서 갈 수 있는 모든 정점들을 방문한다.
# 시작점에서 도착점까지 최단경로를 찾으려면 가능한 모든 경로를 확인해야 한다.
# 깊이 우선탐색은 시작점에서 출발해서 도착점을 처음 방문할 때 최단 경로로 왔다는 것을 보장할 수 없다.
# 너비 우선 탐색은 시작점에서 도착점을 처음 방문할 때 최단 경로를 방문한다.(다만. 간선의 가중치가 없을 때)



