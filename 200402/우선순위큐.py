# 우선 순위 큐 = 삽입한 순서대로 삭제되지 않는다.
# 1. heapq
# 2. queue.PriorityQueue

from heapq import heappush, heappop

arr=[]
heappush(arr,[-3,(3,2)])
heappush(arr,[1,(2,3)])
heappush(arr,[1,(2,1)])
heappush(arr,[1,(2,2)])

while arr:
    print(heappop(arr))

# 작은 순서대로 뽑아온다.
# 우선순위 줄수도 있음


from queue import PriorityQueue

pq = PriorityQueue()
pq.put((3,2))
pq.put((2,3))
pq.put((2,1))
pq.put((2,2))

while not pq.empty():
    print(pq.get())

# 작은 순서대로 뽑아온다.
# 더 깔끔한 방법.
# 최단경로-? 다익스트라 알고리즘을 구현할 때 쓰임.
# 최소신장트리 -> prim 알고리즘
# 허프만트리