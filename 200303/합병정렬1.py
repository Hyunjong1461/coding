def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        if list1[0] > list2[0]:
            return list2[:1] + merge(list1, list2[1:])
        else:
            return list1[:1] + merge(list1[1:], list2)


# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    list1=my_list[:len(my_list)//2]
    list2=my_list[len(my_list)//2:]
    if len(list1) ==1:
        return merge(list1, list2)
    else:
        list1 = merge_sort(list1)
        list2 = merge_sort(list2)
        return merge(list1, list2)



# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
