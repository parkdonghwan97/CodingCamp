from random import randint


def generate_numbers(n):
    numbers = []
    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)
    return numbers


# 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다.
# 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다.

def draw_winning_numbers():
    win = []
    while len(win) < 6:
        num = randint(1, 45)
        if num not in win:
            win.append(num)
    win.sort()
    while len(win) < 7:
        bonus = randint(1, 45)
        if bonus not in win:
            win.append(bonus)

    return win

def count_matching_numbers(list_1, list_2):
    # print(list_1)
    # print(list_2)
    count = 0
    for i in range(len(list_2)):

        if list_2[i] in list_1:

            count += 1
    return count
# 6개 리스트 , 7개 리스트

# 테스트
# print(count_matching_numbers(generate_numbers(6), draw_winning_numbers()))
# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치 (10억 원) P
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치 (5천만 원) P
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치 (100만 원)P
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치 (5만 원)  P
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치 (5천 원)  P

def check(numbers, winning_numbers): #6, 7
    bonus = winning_numbers[-1]
    nomallist = []
    for i in range(len(numbers)): #보너스 번호를 제외한 일반번호들만 담은 리스트 생성
        nomallist.append(winning_numbers[i])

    ck = 0
    bs = 0
    for i in range(len(numbers)):
        if numbers[i] in nomallist:
            ck += 1
        if numbers[i] == bonus:
            bs += 1
    # print(ck)

    if ck == 3:
        return 5000
    elif ck == 4:
        return 50000
    elif ck == 5 and bs ==0 :    # ck만 5개 일치
        return 1000000
    elif ck == 5 and bs == 1:    # ck5개 일치 + bs 1개
        return 50000000
    elif ck == 6:                # ck가 6개면 10억
        return 1000000000
    else:
        return 0



# 테스트
# numbers = generate_numbers(6)
# winning_numbers =  draw_winning_numbers()
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))