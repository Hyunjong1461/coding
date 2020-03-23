def trapping_rain(buildings):
    # 코드를 작성하세요
    startpoint=0
    maxpoint=0
    cnt = 0

    for i in range(len(buildings)):
        if buildings[i]!=0:
            startpoint=i
            break

    for i in range(len(buildings)):
        if buildings[i]==max(buildings):
            maxpoint=i
            break

    for i in range(startpoint,maxpoint+1):
        for j in range(i+1,maxpoint+1):
            if buildings[i]<=buildings[j]:
                for k in range(i+1,j):
                    cnt+=buildings[i]-buildings[k]
                    buildings[k] = buildings[i]
                break
    for i in range(maxpoint+1,len(buildings)):
        for j in range(i+1,len(buildings)):
            if buildings[i]==buildings[j]:
                for k in range(i,j):
                    cnt+=buildings[i]-buildings[k]
                    buildings[k]=buildings[i]
                break


    return cnt


# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))




# def trapping_rain(buildings):
#     # 총 담기는 빗물의 양을 변수에 저장
#     total_height = 0
#
#     # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
#     # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
#     for i in range(1, len(buildings) - 1):
#         # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
#         max_left = max(buildings[:i]) 0부터 i까지
#         max_right = max(buildings[i:]) i부터 끝까지
#
#         # 현재 인덱스에 빗물이 담길 수 있는 높이
#         upper_bound = min(max_left, max_right)
#
#         # 현재 인덱스에 담기는 빗물의 양을 계산
#         # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
#         total_height += max(0, upper_bound - buildings[i])
#
#     return total_height
#
# # 테스트
# print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
# print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))