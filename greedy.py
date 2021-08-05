# def min_coin_count(value, coin_list):
#     coin_list.sort(reverse=True)
#     # print(coin_list)
#     count = 0
#     for i in coin_list:
#         count += value // i
#         # print()
#         value = value % i
#
#     return count
#
#
# # 테스트
# default_coin_list = [100, 500, 10, 50]
# print(min_coin_count(1170, default_coin_list))

## 문제2
# def max_product(card_lists):
#     total = 1
#     for i in card_lists:
#         total *= max(i)
#
#         # total *= max(card_lists)
#     return total
#
#
# # 테스트
# test_cards1 = [[1, 6, 5], [4, 2, 3]]
# print(max_product(test_cards1))
#
# test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
# print(max_product(test_cards2))
#
# test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
# print(max_product(test_cards3))
#
# test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
# print(max_product(test_cards4))

## 문제 3
# def min_fee(pages_to_print):
#     # 페이지 수가 적은것들 먼저
#     pages_to_print.sort()
#     total = 0 # 벌금
#     for i in range(len(pages_to_print)):
#         total += pages_to_print[i] * (len(pages_to_print)-i)
#     return  total
#
#
# # 테스트
# print(min_fee([6, 11, 4, 1]))
# print(min_fee([3, 2, 1]))
# print(min_fee([3, 1, 4, 3, 2]))
# print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
#
#

# 문제 4
def course_selection(course_list):
    # 수업을 끝나는 순서로 정렬한다
    sorted_list = sorted(course_list, key=lambda x: x[1])

    # 가장 먼저 끝나는 수업은 무조건 듣는다
    my_selection = [sorted_list[0]]

    # 이미 선택한 수업과 안 겹치는 수업 중 가장 빨리 끝나는 수업을 고른다
    for course in sorted_list:
        # 마지막 수업이 끝나기 전에 새 수업이 시작하면 겹친다
        if course[0] > my_selection[-1][1]:
            my_selection.append(course)

    return my_selection


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
