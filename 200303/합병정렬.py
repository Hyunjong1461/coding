def merge(list1, list2):
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        if list1[0] < list2[0]:
            return list1[ :1] + merge(list1[1: ], list2)
        else:
            return list2[ :1] + merge(list1, list2[1: ])



# 코드를 작성하세요.

# 테스트
# print(merge([1], []))
# print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))