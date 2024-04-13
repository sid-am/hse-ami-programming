def move(n, x, y):
    print(n, x, y)


def hanoi(n, a, b):
    if n == 1:
        move(n, a, b)
    else:
        t = 6 - a - b
        hanoi(n - 1, a, t)
        move(n, a, b)
        hanoi(n - 1, t, b)


n = int(input())
hanoi(n, 1, 3)
