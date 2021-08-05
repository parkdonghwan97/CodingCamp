def fib_tab(n):

    # n이 0 1, 2
    table = [0, 1, 1]
    if n > 3:
        for i in range(3, n+1):
            a = table[i-2] + table[i-1]
            table.append(a)

    return table[n]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))