from random import randint


def generate_numbers():
    numbers = []
    # for i in range(3):                         # 이렇게 하지말고
    while len(numbers) < 3:  # 새로운 리시트의 길이가 3보다 작을 때!
        num = randint(0, 9)

        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.")
    return numbers


# print(generate_numbers())


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:

        x = int(input(("{}번째 숫자를 입력하세요. : ".format(len(new_guess) + 1))))

        if x in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요.")

        elif x < 0 or x > 9:  # 범위 벗어나는 경우
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue

        else:
            new_guess.append(x)

    return new_guess


# print(take_guess())


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0
end = 0
while end == 0:
    retry = take_guess()
    a, b = get_score(ANSWER, retry)
    print("{}S {}B".format(a, b))

    # print("{}S {}B".format(get_score(ANSWER, retry)))

    tries += 1
    print(ANSWER)
    if a == 3:
        end = 1

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))
