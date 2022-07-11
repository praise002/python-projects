def factorial_recursive(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * factorial_recursive(n - 1)


print(factorial_recursive(5))