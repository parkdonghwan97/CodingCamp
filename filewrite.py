with open('vocabulary.txt', 'r') as f:
    for quiz in f:
        data = quiz.strip().split(": ")
        english, korean = data[0], data[1]          # 영어는 0번, 한국어는 1번 인덱스

        # 유저 입력값 받기
        check = input("{}: ".format(korean))

        # 정답 확인하기
        if check == english:
            print("정답입니다!")
            print()
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(english))
            print()