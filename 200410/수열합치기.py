import sys
sys.stdin = open('5120.txt','r')
#
class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail = None
        self.size = 0


def addLast(lst, new):
    if lst.head is None:
        lst.head = new
        new.prev = new.next = new
    else:
        tail = lst.head.prev

        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new

        # 새로 추가 되는 노드를 업데이트 하고 나서, 나머지 업데이트 해야한다.
    lst.size += 1


def printList(lst):
    if lst.head is None:
        return
    # cur = lst.head
    # for _ in range(lst.size):
    #     print(cur.data, end=' ')
    #     cur = cur.next
    # print()

    cur = lst.head.prev

    for _ in range(lst.size):
        # print(cur.data, end=' ')
        result.append(cur.data)
        cur = cur.prev


# mylist = LinkedList()
# arr = [6, 2, 4, 9, 1, 5]
# for val in arr:
#     addLast(mylist, Node(val))
# printList(mylist)

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    mylist = LinkedList()
    arr = list(map(int, input().split()))
    for val in arr:
        addLast(mylist,Node(val))
    cur = mylist.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next

        prev = cur.prev
        new = Node(prev.data + cur.data,prev,cur)
        prev.next = new
        cur.prev = new
        cur = new   # 새로 추가된 위치를 시작 위치로 재설정
        mylist.size += 1
    result = []
    printList(mylist)

    print('#{} '.format(tc),end='')
    for i in range(N+K):
        if i >= 10:
            break
        print(result[i], end=' ')
    print()