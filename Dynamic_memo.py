def fib_memo(n, cache):
    # fib(1), fib(2) = 1
    if n <= 2:
        return 1

    # 계산된 값이 있다면 캐시에서 꺼냄
    if n in cache:
        return cache[n]

    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
