#단일(단순) 연결리스트
class Node:
    def __init__(self, d=0, n=None):
        self.data =d    #정수 값

        self.next =n    #다음 노드 주소
        # print(d,'생성')

    # def __del__(self):
    #     print(self.data, '삭제')

class LinkedList:
    def __init__(self):
        self.head = None    #첫번 째 노드
        self.tail = None    #마지막 노드
        self.size = 0       #노드의 수

mylist =LinkedList()

def printList(lst): #lst =LinkedList 객체
    if lst.head == None: return
    cur = lst.head
    print(lst.size, '[', end=' ')

    while cur is not None:
        print(cur.data, end=' ')
        cur=cur.next
    print(']')

def insertLast(lst,new): # new : 새로 추가할 노드 객체
    #빈 리스트 일 경우
    if lst.head is None:
        lst.head=lst.tail=new
    else:
        lst.tail.next =new
        lst.tail=new
        # #마지막 노드를 찾는다.
        #
        # cur = lst.head
        # while cur.next is not None:
        #     cur = cur.next
        #
        # cur.next=new
    lst.size +=1

def deleteLast(lst):
    pass

for i in range(5):
    insertLast(mylist,Node(i))
    printList(mylist)

while mylist.size:
    deleteLast(mylist)
    printList(mylist)
# n5 = Node(5); n4 = Node(4,n5); n3 = Node(3,n4);
# n2 =Node(2,n3); n1 =Node(1,n2)
#
# mylist.head =n1; mylist.size = 5
