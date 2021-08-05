def merge(list1, list2):
    mergelist = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            mergelist.append(list2[j])
            j += 1
        else:
            mergelist.append(list1[i])
            i += 1

    # 하나의 리스타가 모두 소진시, 다른 리스트 합체
    if i == len(list1):
        return mergelist + list2[j:]
    else:
        return mergelist + list1[i:]


def merge_sort(my_list):
    # base case = 리스트 인덱스가 비어있거나 1개일때
    if len(my_list) < 2:
        return my_list

    # 리스트를 반띵해야댐
    mid = len(my_list) // 2
    left = my_list[:mid]
    right = my_list[mid:]

    # 여기가 너무 어렵다.
    # merge_sort를  반띵한 왼쪽과 오른쪽 리스트를 재귀적으로 호출하고
    # merge 함수를 통해 정렬된 두 리스트를 합침
    # return merge(merge_sort(my_list[left]), merge_sort(my_list[right])) 안되는 이유가 있지.
    return merge(merge_sort(left), merge_sort(right))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
