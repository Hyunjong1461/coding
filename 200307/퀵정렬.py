# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1],my_list[index2]=my_list[index2],my_list[index1]

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    b=start
    i=start
    p=end
    pivot=my_list[p]
    while 1:
        if i==end:
            break
        elif pivot>my_list[i]:
            swap_elements(my_list, b, i)
            b+=1
            i+=1
        else:
            i+=1
    swap_elements(my_list, b, i)
    return b

def quicksort(my_list, start=0, end=None):
    # 코드를 작성하세요.
    if end == None:
        end = len(my_list) - 1

    if end-start<0:
        return
    else:
        quicksort(my_list, partition(my_list, start, end) + 1, end)
        quicksort(my_list, start, partition(my_list, start, end)-1)






# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1) # start, end 파라미터 없이 호출
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2) # start, end 파라미터 없이 호출
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3) # start, end 파라미터 없이 호출
print(list3)
