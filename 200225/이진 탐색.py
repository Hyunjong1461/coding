def binary_search(element, some_list):
    # 코드를 작성하세요.
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

    # flag=0
    # while 1:
    #     midpoint = (start_index + end_index) // 2
    #     if some_list[midpoint]==element:
    #         flag=1
    #         break
    #     elif some_list[midpoint+1]==element:
    #         flag=2
    #         break
    #     elif start_index==end_index:
    #         if some_list[midpoint]!=element:
    #             break
    #     elif some_list[midpoint]<element:
    #         start_index=midpoint
    #     elif some_list[midpoint]>element:
    #         end_index=midpoint
    #
    # if flag ==1:
    #     return midpoint
    # elif flag ==2:
    #     return midpoint+1
    # else:
    #     return





# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))